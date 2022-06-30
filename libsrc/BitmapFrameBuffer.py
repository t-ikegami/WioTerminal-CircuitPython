from micropython import const
import displayio as dpio
import bitmaptools as bmt
from terminalio import FONT

LEFT   = const(0)
RIGHT  = const(1)
CENTER = const(2)

def setup_framebuffer(width, height, depth) :
    bmp = dpio.Bitmap(width, height, depth)
    pal = dpio.Palette(depth)
    return BitmapFrameBuffer(bmp, pal)

def setup_standard_display(vertical = False) :
    if vertical :
        bf = setup_framebuffer(240, 320, 16)
        bf.transpose_xy = True
        bf.flip_x = True
    else :
        bf = setup_framebuffer(320, 240, 16)

    bf.set_palette( 0, 0x000000, "Black")
    bf.set_palette( 1, 0x0000FF, "Blue")
    bf.set_palette( 2, 0x00FF00, "Green")
    bf.set_palette( 3, 0x00FFFF, "Cyan")
    bf.set_palette( 4, 0xFF0000, "Red")
    bf.set_palette( 5, 0xFF00FF, "Magenta")
    bf.set_palette( 6, 0xFFFF00, "Yellow")
    bf.set_palette( 7, 0xFFFFFF, "White")
    bf.set_palette( 8, 0x808080, "Gray")
    bf.set_palette( 9, 0x7B007B, "Purple")
    bf.set_palette(10, 0xADFF29, "GreenYellow")
    bf.set_palette(11, 0x7B7D00, "Olive")
    bf.set_palette(12, 0x7B0000, "Maroon")
    bf.set_palette(13, 0xFF82C6, "Pink")
    bf.set_palette(14, 0xFFA500, "Orange")
    bf.set_palette(15, 0xC6C6C6, "LightGray")

    return bf

class BitmapFrameBuffer (dpio.TileGrid) :	# originally implemented as a subclass of adafruit_framebuf
    
    def __init__(self, bitmap, palette) :
        super().__init__(bitmap, pixel_shader = palette)
        self.bmp = bitmap
        self.pal = palette

    @property
    def width(self) :
        return self.bmp.width

    @property
    def height(self) :
        return self.bmp.height
        
    def fill(self, color):
        """Fill the entire FrameBuffer with the specified color."""
        self.bmp.fill(color)

    def pixel(self, x, y, color = None):
        """If color is not given, get the color value of the specified
        pixel. If color is given, set the specified pixel to the given
        color.

        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height : return None
        if color is None: return self.bmp[x, y]
        self.bmp[x, y] = color
        return None

    def hline(self, x, y, width, color):
        """Draw a horizontal line up to a given length."""
        if y < 0 or y >= self.height : return
        w = x + width
        if w < 0 or x >= self.width : return
        x = max(x, 0)
        w = min(w, self.width - 1)
        bmt.draw_line(self.bmp, x, y, w, y, color)

    def vline(self, x, y, height, color):
        """Draw a vertical line up to a given length."""
        if x < 0 or x >= self.width : return
        w = y + height
        if w < 0 or y >= self.height: return
        y = max(y, 0)
        w = min(w, self.height - 1)
        bmt.draw_line(self.bmp, x, y, x, w, color)

    def line(self, x0, y0, x1, y1, color):
        """Draw line with clipping"""

        if x0 == x1 : return self.vline(x0, min(y0, y1), abs(y0 - y1), color)
        if y0 == y1 : return self.hline(min(x0, x1), y0, abs(x0 - x1), color)
        
        xmax = self.width - 1
        ymax = self.height -1
        
        def LocationCode(x, y) :
            code = 0
            
            if x < 0 : code |= 1
            elif x > xmax : code |= 2
            if y < 0 : code |= 4
            elif y > ymax : code |= 8
            
            return code

        code0 = LocationCode(x0, y0)
        code1 = LocationCode(x1, y1)

        while True :
            if (code0 | code1) == 0 : break	# both inside
            if (code0 & code1) : return		# no cross section

            code = code1 if code0 == 0 else code0
            if code & 3 :	# x < 0 or x > xmax
                x = 0 if code & 1 else xmax
                y = y0 + (y1 - y0) * (x - x0) // (x1 - x0)
            else : # y < 0 or y > ymax
                y = 0 if code & 4 else ymax
                x = x0 + (x1 - x0) * (y - y0) // (y1 - y0)

            if code0 == 0 :
                x1, y1 = x, y
                code1 = LocationCode(x1, y1)
            else :
                x0, y0 = x, y
                code0 = LocationCode(x0, y0)

        bmt.draw_line(self.bmp, x0, y0, x1, y1, color)

    def rect(self, x, y, width, height, color, *, fill=False):
        """Draw a rectangle at the given location, size and color. The ```rect``` method draws only
        a 1 pixel outline."""

        if fill is False :
            width  -= 1
            height -= 1
            self.hline(x, y, width,  color)
            self.vline(x, y, height, color)
            self.hline(x, y + height, width, color)
            self.vline(x + width, y, height, color)
            return
        
        if x >= self.width or y >= self.height : return
        if x + width <= 0 or y + height <= 0 : return
        x = max(x, 0)
        y = max(y, 0)
        x1 = min(x + width,  self.width)
        y1 = min(y + height, self.height)
        bmt.fill_region(self.bmp, x, y, x1, y1, color)

    def set_palette(self, idx, color, name = None) :
        if name is None and isinstance(color, str) : (color, name) = (None, color)
        if color is not None : self.pal[idx] = color
        if name  is not None : setattr(self, name, idx)
        
    def polyline(self, points, color, *, close = True):
        for i in range(len(points) - 1) :
            self.line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], color)
        if close :
            self.line(points[-1][0], points[-1][1], points[0][0], points[0][1], color)

    def triangle(self, p0, p1, p2, color, *, fill=False):
        if fill is False :
            self.polyline([p0, p1, p2], color)
            return

        # Sort coordinates by Y order (y2 >= y1 >= y0)
        if p0[1] > p1[1] : p0, p1 = p1, p0
        if p1[1] > p2[1] : p1, p2 = p2, p1
        if p0[1] > p1[1] : p0, p1 = p1, p0

        (x0, y0) = p0
        (x1, y1) = p1
        (x2, y2) = p2

        if y0 == y2 : return

        class slope:
            """Should p0[1] < p1[1]"""
            def __init__(self, p0, p1) :
                dx = p1[0] - p0[0]
                dy = p1[1] - p0[1]
                self.sx = dx // dy	# dx = sx * dy + ex, sign(ex) == sign(dy)
                self.ex = dx %  dy
                self.er = 0
                self.x  = p0[0]
                self.dy = dy

            def step(self) :
                self.x  += self.sx
                self.er += self.ex
                if self.er > self.dy :
                    self.er -= self.dy
                    self.x  += 1
                return self.x

        # Upper Triangle
        x02 = slope(p0, p2)
        a = p0[0]
        if y0 < y1 :
            x01 = slope(p0, p1)
            self.pixel(p0[0], p0[1], color)
            for y in range(p0[1]+1, p1[1]+1):
                a = x02.step()
                b = x01.step()
                if a > b: a, b = b, a
                self.hline(a, y, b-a, color)
            
        # Lower Triangle
        if y1 < y2 :
            x12 = slope(p1, p2)
            b = p1[0]
            if a > b: a, b = b, a
            self.hline(a, p1[1], b-a, color)
            for y in range(p1[1]+1,  p2[1]+1):
                a = x02.step()
                b = x12.step()
                if a > b: a, b = b, a
                self.hline(a, y, b-a, color)
            
    def circle(self, center_x, center_y, radius, color, *, fill = False):
        """Draw a circle at the given midpoint location, radius and color.
        The ```circle``` method draws only a 1 pixel outline."""
        # http://fussy.web.fc2.com/algo/algo2-1.htm

        x = radius
        y = 0
        F = 3 - (radius << 1)

        if fill :
            while x >= y:
                self.hline(center_x - x, center_y + y, x << 1, color)
                self.hline(center_x - x, center_y - y, x << 1, color)
                self.hline(center_x - y, center_y + x, y << 1, color)
                self.hline(center_x - y, center_y - x, y << 1, color)
                if F >= 0 :
                    x -= 1
                    F -= x << 2
                y += 1
                F += 2 + (y << 2)
        else :
            while x >= y:
                self.pixel(center_x + x, center_y + y, color)
                self.pixel(center_x + y, center_y + x, color)
                self.pixel(center_x - y, center_y + x, color)
                self.pixel(center_x - x, center_y + y, color)
                self.pixel(center_x - x, center_y - y, color)
                self.pixel(center_x - y, center_y - x, color)
                self.pixel(center_x + y, center_y - x, color)
                self.pixel(center_x + x, center_y - y, color)
                if F >= 0 :
                    x -= 1
                    F -= x << 2
                y += 1
                F += 2 + (y << 2)

    def roundrect(self, x, y, width, height, radius, color, *, fill = False):
        """Draw a roundrect"""
        
        cx0 = x + radius
        cx1 = x + width - radius
        cy0 = y + radius
        cy1 = y + height - radius
        
        px = radius
        py = 0
        F = 3 - (radius << 1)

        if fill :
            w = width - (radius << 1)
            while px >= py:
                self.hline(cx0 - px, cy0 - py, w + (px << 1), color)
                self.hline(cx0 - px, cy1 + py, w + (px << 1), color)
                self.hline(cx0 - py, cy0 - px, w + (py << 1), color)
                self.hline(cx0 - py, cy1 + px, w + (py << 1), color)
                if F >= 0 :
                    px -= 1
                    F -= px << 2
                py += 1
                F += 2 + (py << 2)
            self.rect(x, cy0, width, cy1 - cy0, color, fill = True)
        else :
            while px >= py:
                self.pixel(cx0 - px, cy0 - py, color)
                self.pixel(cx1 + px, cy0 - py, color)
                self.pixel(cx0 - px, cy1 + py, color)
                self.pixel(cx1 + px, cy1 + py, color)
                self.pixel(cx0 - py, cy0 - px, color)
                self.pixel(cx1 + py, cy0 - px, color)
                self.pixel(cx0 - py, cy1 + px, color)
                self.pixel(cx1 + py, cy1 + px, color)
                if F >= 0 :
                    px -= 1
                    F -= px << 2
                py += 1
                F += 2 + (py << 2)
            self.hline(cx0, y,          cx1 - cx0, color)
            self.hline(cx0, y + height, cx1 - cx0, color)
            self.vline(x,         cy0, cy1 - cy0, color)
            self.vline(x + width, cy0, cy1 - cy0, color)
                
    def blit(self, *param, **keys) :
        self.bmp.blit(*param, **keys)

    def rotozoom(self, src, **keys) :
        bmt.rotozoom(self.bmp, src, **keys)
        
    def paint(self, x, y, color, target) :
        """Replace target color starting at (x, y) with color."""

        bmt.boundary_fill(self.bmp, x, y, color, target)
        
    def draw_char(self, x, y, c, color, bgcolor = None, size = 1, font = FONT) :
        """Draw character with terminal font"""
        # (x0,y0) <- (x,y) is updated here
        #    +--------+
        #    |   ..   |
        #    |  .  .  |
        #    | ...... |
        #    | .    . |
        #    | .    . |
        #    +--------+
        #  (x,y)   (x1,y1)
        c = font.get_glyph(ord(c))
        if c is None : return 0
        x += c.dx * size
        y -= (c.height + c.dy) * size
        x0 = max(x, 0)
        y0 = max(y, 0)
        x1 = min(x + size * c.width,  self.width)
        y1 = min(y + size * c.height, self.height)
        if x0 >= x1 or y0 >= y1 : return c.shift_x * size
        ox = c.tile_index * c.width * size - x
        oy = -y
        for y in range(y0, y1) :
            for x in range(x0, x1) :
                if c.bitmap[(ox + x)//size, (oy + y)//size] :
                    self.bmp[x, y] = color
                elif bgcolor is not None :
                    self.bmp[x, y] = bgcolor
        return c.shift_x * size

    def text_width(self, txt, size = 1, font = FONT) :
        def get_width(c) :
            c = font.get_glyph(ord(c))
            return 0 if c is None else c.shift_x
        
        return sum( get_width(c) for c in txt ) * size

    def draw_text(self, x, y, txt, color, bgcolor = None, align = LEFT, size = 1,
                  font = FONT, line_height = None) :
        """Draw text at the baseline position (x,y).  Terminal font is used by
        default, or pass adafruit_bitmap_font.

        """
        if line_height is None : line_height = font.get_bounding_box()[1] * size
        iy = y
        for line in txt.split("\n") :
            l = self.text_width(line, size, font)
            ix = x          if align == LEFT  else \
                 x - l      if align == RIGHT else \
                 x - l // 2
            for c in line :
                ix += self.draw_char(ix, iy, c, color, bgcolor, size, font)
            iy += line_height
        return (ix, iy - line_height)
        
if __name__ == "__main__" :
    import board
    import displayio as dpio

    disp = board.DISPLAY
    bm = dpio.Bitmap(300, 200, 8)
    pl = dpio.Palette(8)
    for i in range(8) :
        pl[i] = (0xFF0000 if i & 4 else 0) + (0xFF00 if i & 2 else 0) + (0xFF if i & 1 else 0)

    g = dpio.Group()
    g.append(dpio.TileGrid(bm, pixel_shader = pl, x = 10, y = 20))
    disp.show(g)
        
    bf = BitmapFrameBuffer(bm, pl)
    
