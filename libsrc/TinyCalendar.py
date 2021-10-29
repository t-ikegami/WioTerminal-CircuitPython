import time
import displayio as dpio
from BitmapFrameBuffer import BitmapFrameBuffer, CENTER

def get_mdays(tm) :
    m = tm.tm_mon
    d = 31
    if m in (4, 6, 9, 11) : d = 30
    if m != 2 : return d

    t = time.struct_time((tm.tm_year, m, 29, 0, 0, 0, -1, -1, -1))
    t = time.localtime(time.mktime(t))
    return 29 if t.tm_mon == m else 28

def get_1wday(tm) :
    t = time.struct_time((tm[0], tm[1], 1, 0, 0, 0, -1, -1, -1))
    t = time.localtime(time.mktime(t))
    return t.tm_wday

class Calendar (dpio.TileGrid) :
    
    def __init__(self, tm = None) :
        if tm is None : tm = time.localtime()

        bmp = dpio.Bitmap(120, 100, 4)
        pal = dpio.Palette(4)
        bf  = BitmapFrameBuffer(bmp, pal)
        bf.set_palette(0, 0xFFFFFF, "Back")
        bf.set_palette(1, 0x000000, "Fore")
        bf.set_palette(2, 0xFF0000, "Red" )
        bf.set_palette(3, 0x0000FF, "Blue")
        
        super().__init__(bmp, pixel_shader = pal)
        self.bf = bf
        self.show_calendar(tm)

    def show_calendar(self, tm, mark = None) :
        bf = self.bf
        bf.fill(bf.Back)
        bf.draw_text(60, 15, f"{tm.tm_year} / {tm.tm_mon}", bf.Fore, align = CENTER)
        (x, y) = bf.draw_text( 6, 27, "SU", bf.Red )
        (x, y) = bf.draw_text( x + 4, y, "MO", bf.Fore)
        (x, y) = bf.draw_text( x + 4, y, "TU", bf.Fore)
        (x, y) = bf.draw_text( x + 4, y, "WE", bf.Fore)
        (x, y) = bf.draw_text( x + 4, y, "TH", bf.Fore)
        (x, y) = bf.draw_text( x + 4, y, "FR", bf.Fore)
        bf.draw_text( x + 4, y, "SA", bf.Blue)

        ofs = get_1wday(tm)
        if ofs == 6 : ofs = -1

        def get_pos(d) :
            (y, x) = divmod(d + ofs, 7)
            color = bf.Red  if x == 0 else \
                    bf.Blue if x == 6 else \
                    bf.Fore
            
            y = 41 + y * 12
            x = 12 + x * 16
            return (x, y, color)
            
        for d in range(1, get_mdays(tm) + 1) :
            (x, y, color) = get_pos(d)
            bf.draw_text(x, y, str(d), color, align = CENTER)

        if mark is None : mark = tm[:3] == time.localtime()[:3]
        if mark :
            d = tm.tm_mday
            (x, y, _) = get_pos(d)
            bf.draw_text(x, y, str(d), bf.Back, bf.Fore, align = CENTER)

#------------------------------------------------------------------------
# import board
# from ButtonEvents import ButtonEvents
#
# tm = time.localtime()
# disp = board.DISPLAY
# g = dpio.Group()
# c = Calendar(tm)
# g.append(c)
# g.scale = 2
# g.x = 40
# g.y = 20
# disp.show(g)
# 
# y = tm.tm_year
# m = tm.tm_mon
# d = tm.tm_mday
# 
# be = ButtonEvents()
# 
# while True :
#     time.sleep(0.05)
#     b = be.keys()
#     if b == 0 : continue
# 
#     if   b & be.K_SELECT : break
#     elif b & be.K_O      :
#         tm = time.localtime()
#         y = tm.tm_year
#         m = tm.tm_mon
#         d = tm.tm_mday
#     elif b & be.K_UP    : y -= 1
#     elif b & be.K_DOWN  : y += 1
#     elif b & be.K_LEFT  :
#         if m > 1 : m -= 1
#         else :
#             y -= 1
#             m = 12
#     elif b & be.K_RIGHT :
#         if m < 12 : m += 1
#         else :
#             y += 1
#             m = 1
# 
#     c.show_calendar(time.struct_time((y, m, d, 0, 0, 0, -1, -1, -1)))
# 
# be.deinit()
# disp.show(None)
