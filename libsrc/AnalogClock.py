import math
import displayio as dpio
import vectorio as vio
from BitmapFrameBuffer import BitmapFrameBuffer, CENTER

class Hand :
    def __init__(self, ox, oy, length, width, offset, color) :
        self.ox = ox
        self.oy = oy
        self.length = length
        self.width  = width
        self.offset = offset
        self.angle = None

        self.pal = dpio.Palette(1)
        self.set_color(color)

        self.poly = vio.Polygon( pixel_shader = self.pal,
                                 points = [(0, 0), (0, 0), (0, 0), (0, 0)] )

        self.set_angle(0)
 
    def set_color(self, color) :
        self.pal[0] = color
        
    def set_angle(self, th) :
        if self.angle == th : return
        self.angle = th
        th = (th - 90) * math.pi / 180
        x = math.cos(th)
        y = math.sin(th)
        lx = self.ox + self.length * x
        ly = self.oy + self.length * y
        ox = self.ox - self.offset * x
        oy = self.oy - self.offset * y
        wx =   self.width * y / 2.0
        wy = - self.width * x / 2.0
        self.poly.points = [( round(ox + wx), round(oy + wy) ),
                            ( round(lx + wx), round(ly + wy) ),
                            ( round(lx - wx), round(ly - wy) ),
                            ( round(ox - wx), round(oy - wy) )]
        
class Clock (dpio.Group) :
    def __init__(self, size = 200) :
        super().__init__()
        s = size // 2
        self.size = size
        self.face = self.setup_face()
        self.hour = Hand(s, s, s * 5 // 10, s // 20, s // 10, 0xFFFFFF)
        self.min  = Hand(s, s, s * 7 // 10, s // 25, s // 10, 0xFFFFFF)
        self.sec  = Hand(s, s, s * 8 // 10, s // 50, s // 5,  0xFF0000)
        self.daytime = False

        self.append(self.face)
        self.append(self.hour.poly)
        self.append(self.min.poly)
        self.append(self.sec.poly)

    def setup_face(self) :
        s = self.size // 2
        bmp = dpio.Bitmap(self.size, self.size, 4)
        pal = dpio.Palette(4)
        bf = BitmapFrameBuffer(bmp, pal)

        bf.set_palette(0, 0x000000, "Back")
        bf.set_palette(1, 0x606060, "Face")
        bf.set_palette(2, 0xC8C8C8, "Dot")
        bf.set_palette(3, 0xFFFFFF, "Fore")

        bf.circle(s, s, s - 1,     bf.Dot,  fill = True)
        bf.circle(s, s, s - s//25, bf.Face, fill = True)

        r1 = s - s *  8 // 100	# dot
        d1 = s * 1 // 100
        r2 = s - s * 20 // 100	# number
        d2 = s * 3 // 100
        for i in range(0, 360, 6) :
          th = i * math.pi / 180
          ix = s + int(r1 * math.cos(th))
          iy = s + int(r1 * math.sin(th))
          bf.circle(ix, iy, d1, bf.Dot, fill = True)

        for i in range(1, 13) :
          th = (i * 30 - 90) * math.pi / 180
          x = math.cos(th)
          y = math.sin(th)
          
          ix = s + int(r1 * x)
          iy = s + int(r1 * y)
          bf.circle(ix, iy, d2, bf.Dot, fill = True)

          ix = s + int(r2 * x)
          iy = s + int(r2 * y) + 7
          bf.draw_text(ix, iy, str(i), bf.Fore, align = CENTER)

        return bf

    def set_time(self, hour, min, sec = None) :
        """Set hands to the time specified.  If sec is omitted, the second
        hand is hidden.  The colors of face/hands are changed
        according to time.  To suppress the color change, set daytime
        attribute to None.  To force the color reset, set daytime to
        -1.

        """
        if sec is None :
            sec = 0
            if self[-1] is self.sec.poly : self.pop()
        else :
            if self[-1] is not self.sec.poly : self.append(self.sec.poly)
        
        self.hour.set_angle(hour * 30 + min // 2)
        self.min.set_angle(min * 6 + sec // 10)
        self.sec.set_angle(sec * 6)

        if self.daytime is None : return
        daytime = (6 <= hour < 18)
        if self.daytime == daytime : return
        
        self.daytime = daytime
        bf = self.face
        if daytime :
            bf.set_palette(bf.Back, 0x000000)
            bf.set_palette(bf.Face, 0xFFFFFF)
            bf.set_palette(bf.Dot,  0xC8C8C8)
            bf.set_palette(bf.Fore, 0x000000)
            self.hour.set_color(0x000000)
            self.min.set_color(0x000000)
        else :
            bf.set_palette(bf.Back, 0x000000)
            bf.set_palette(bf.Face, 0x606060)
            bf.set_palette(bf.Dot,  0xC8C8C8)
            bf.set_palette(bf.Fore, 0xFFFFFF)
            self.hour.set_color(0xFFFFFF)
            self.min.set_color(0xFFFFFF)

