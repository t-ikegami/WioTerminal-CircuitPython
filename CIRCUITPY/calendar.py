import time
import board
import displayio as dpio
from RictyKanji import draw_text, set_palette, han2zen
from ButtonEvents import ButtonEvents
from TinyCalendar import get_mdays, get_1wday

class Calendar (dpio.TileGrid) :
    black = (0,  1,  2,  3)
    gray  = (0,  4,  5,  6)
    red   = (0,  7,  8,  9)
    blue  = (0, 10, 11, 12)
    rev   = (3, 13, 14, 15)
    
    def __init__(self, tm = None) :
        if tm is None : tm = time.localtime()

        bmp = dpio.Bitmap(320, 240, 16)
        pal = dpio.Palette(16)
        set_palette(pal, bg = 0xFFFFFF, fg = 0x000000, map = self.black, bold = False)
        set_palette(pal, bg = 0xFFFFFF, fg = 0x808080, map = self.gray,  bold = False)
        set_palette(pal, bg = 0xFFFFFF, fg = 0xFF0000, map = self.red,   bold = False)
        set_palette(pal, bg = 0xFFFFFF, fg = 0x0000FF, map = self.blue,  bold = False)
        set_palette(pal, bg = 0x000000, fg = 0xFFFFFF, map = self.rev,   bold = True)
        
        super().__init__(bmp, pixel_shader = pal)
        self.bmp = bmp
        self.pal = pal

        self.show_calendar(tm)

    def show_calendar(self, tm, mark = None) :
        self.bmp.fill(0)
        txt = han2zen(f"{tm.tm_year}年{tm.tm_mon}月")
        draw_text(self.bmp, 160 - len(txt) * 8, 7, txt, map = self.black)
        draw_text(self.bmp,  32, 37, "日", map = self.red)
        draw_text(self.bmp,  72, 37, "月", map = self.black)
        draw_text(self.bmp, 112, 37, "火", map = self.black)
        draw_text(self.bmp, 152, 37, "水", map = self.black)
        draw_text(self.bmp, 192, 37, "木", map = self.black)
        draw_text(self.bmp, 232, 37, "金", map = self.black)
        draw_text(self.bmp, 272, 37, "土", map = self.blue)

        ofs = get_1wday(tm)
        if ofs == 6 : ofs = -1

        def get_pos(d) :
            (y, x) = divmod(d + ofs, 7)
            map = self.red  if x == 0 else \
                  self.blue if x == 6 else \
                  self.black
            
            y = 67 + y * 30
            x = 32 + x * 40
            if d >= 10 : x -= 8
            return (x, y, map)
            
        for d in range(1, get_mdays(tm) + 1) :
            (x, y, map) = get_pos(d)
            draw_text(self.bmp, x, y, han2zen(str(d)), map = map)

        if mark is None : mark = tm[:3] == time.localtime()[:3]
        if mark :
            d = tm.tm_mday
            (x, y, map) = get_pos(d)
            draw_text(self.bmp, x, y, han2zen(str(d)), map = self.rev)

#------------------------------------------------------------------------
# from TinyCalendar import Calendar

tm = time.localtime()
disp = board.DISPLAY
g = dpio.Group()
c = Calendar(tm)
g.append(c)
# g.scale = 2
# g.x = 40
# g.y = 20
disp.show(g)

y = tm.tm_year
m = tm.tm_mon
d = tm.tm_mday

be = ButtonEvents()

while True :
    time.sleep(0.05)
    b = be.keys()
    if b == 0 : continue

    if   b & be.K_SELECT : break
    elif b & be.K_O      :
        tm = time.localtime()
        y = tm.tm_year
        m = tm.tm_mon
        d = tm.tm_mday
    elif b & be.K_UP    : y -= 1
    elif b & be.K_DOWN  : y += 1
    elif b & be.K_LEFT  :
        if m > 1 : m -= 1
        else :
            y -= 1
            m = 12
    elif b & be.K_RIGHT :
        if m < 12 : m += 1
        else :
            y += 1
            m = 1

    c.show_calendar(time.struct_time((y, m, d, 0, 0, 0, -1, -1, -1)))

be.deinit()
disp.show(None)




