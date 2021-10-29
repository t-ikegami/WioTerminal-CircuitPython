from array import array
import displayio as dpio
import adafruit_imageload as imgload
from Cursor import Cursor

class PixelDisplay(dpio.Group) :
    # (10x10) x 16 tiles
    pix_bmp, pix_pal = imgload.load("Pixel.bmp", bitmap = dpio.Bitmap, palette = dpio.Palette)

    def __init__(self, width = 16, height = 16) :
        super().__init__()
        self.pix = dpio.TileGrid(self.pix_bmp, pixel_shader = self.pix_pal,
                                 width = width, height = height,
                                 tile_width = 10, tile_height = 10)
        self.append(self.pix)
        self.width = width
        self.height = height

        self.cur = Cursor( 12, 12,
                           (-1, -1),
                           ((width - 1) * 10 - 1, (height - 1) * 10 - 1),
                           (10, 10) )
        self.append(self.cur)
        self.cur.set_color(False)
        
    def fill(self, val) :
        for i in range(self.width * self.height) : self.pix[i] = val

    def dump(self) :
        size = self.width * self.height
        data = bytearray( (size + 1) // 2 )
        for i in range(size) :
            data[i // 2] |= self.pix[i] << (4 if i & 1 else 0)
        return data
    
    def restore(self, data) :
        size = self.width * self.height
        for i in range(size) :
            self.pix[i] = data[i // 2] >> 4 if i & 1 else data[i // 2] & 0xf
        
    def edit(self) :
        pix = self.pix
        cur = self.cur

        cur.set_color(0xA0A000)
        cur.locate(0, 0)
        pen = False
        color = 0
        while True:
            ev = cur.get_event(motion = pen)
            (x, y) = (cur.cx, cur.cy)
            if ev[0] is None :
                if   ev[1] == 0  : break
                elif ev[1] == 1  : color = pix[x, y] = (pix[x, y] - 1) & 0xf
                elif ev[1] == 2  : color = pix[x, y] = (pix[x, y] + 1) & 0xf
                elif ev[1] == 20 : pix[x, y] = color		# motion event
            else :
                if pix[x, y] == color :
                    pen = not pen
                    cur.set_color(0xFFFF00 if pen else 0xA0A000)
                else :
                    pix[x, y] = color
        cur.set_color(False)

    def blit(self, x, y, bmp, *, x1 = 0, y1 = 0, x2 = None, y2 = None, map = None) :
        if x2 is None : x2 = min(bmp.width,  x1 + self.width  - x)
        if y2 is None : y2 = min(bmp.height, y1 + self.height - y)
        if map is None : map = array("B", range(16))

        pix = self.pix
        for i in range(x2 - x1) :
            for j in range(y2 - y1) :
                pix[x + i, y + j] = map[bmp[x1 + i, y1 + j]]

    def scroll(self, bmp, y = 0, x1 = 0, x2 = None, delay = 0.1, map = None) :
        import time

        if x2 is None : x2 = bmp.width 
        if map is None : map = array("B", range(16))
        for x in range(x1, x2 - self.width) :
            self.blit(0, y, bmp, x1 = x, map = map)
            time.sleep(delay)

            
class PixelThumb(dpio.Group) :

    pal = dpio.Palette(16)
    for i in range(8) :
        r = 1 if (i & 0x4) else 0
        g = 1 if (i & 0x2) else 0
        b = 1 if (i & 0x1) else 0
        pal[i]     = 0xFF0000 * r + 0x00FF00 * g + 0x0000FF * b
        pal[i + 8] = 0x800000 * r + 0x008000 * g + 0x000080 * b
    pal[8] = 0x404040

    def __init__(self, width = 16, height = 16, nx = 1, ny = 12) :
        super().__init__()
        self.width  = width
        self.height = height
        self.nx     = nx
        self.ny     = ny
        self.bmp = dpio.Bitmap( (width + 2) * nx, (height + 2) * ny, 16)
        self.tg  = dpio.TileGrid(self.bmp, pixel_shader = self.pal)
        self.append(self.tg)

        self.cur = Cursor( width + 2, height + 2,
                           (0, 0),
                           ((width + 2) * (nx - 1), (height + 2) * (ny - 1)),
                           (width + 2, height + 2) )
        self.append(self.cur)

    def get(self, x, y) :
        data = bytearray( (self.width * self.height + 1) // 2 )
        ox = (self.width  + 2) * x
        oy = (self.height + 2) * y
        i = 0
        for y in range(self.height) :
            for x in range(self.width) :
                data[i // 2] |= self.bmp[ox + x + 1, oy + y + 1] << (4 if i & 1 else 0)
                i += 1
        return data
    
    def set(self, x, y, data) :
        ox = (self.width  + 2) * x
        oy = (self.height + 2) * y
        i = 0
        for y in range(self.height) :
            for x in range(self.width) :
                self.bmp[ox + x + 1, oy + y + 1] = data[i // 2] >> 4 if i & 1 else data[i // 2] & 0xf
                i += 1

    def edit(self, d) :
        cur = self.cur
        while True:
            ev = cur.get_event()

            if ev[0] is None :
                if   ev[1] == 0 : return None
                elif ev[1] == 1 : return self.get(cur.cx, cur.cy)
                elif ev[1] == 2 :
                    self.set(cur.cx, cur.cy, d)
                    return (cur.cx, cur.cy)
