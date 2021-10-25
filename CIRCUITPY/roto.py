import math
import board
import displayio as dpio
import bitmaptools as bmt
from BitmapFrameBuffer import BitmapFrameBuffer, CENTER
from MotionEvents import MotionEvents
from ButtonEvents import ButtonEvents

bmp = dpio.Bitmap(320, 240, 2)
pal = dpio.Palette(2)
pal[1] = 0xFFFFFF

src = dpio.Bitmap(150, 150, 2)
src.fill(1)
bf = BitmapFrameBuffer(src, pal)
bf.triangle((75, 25), (25, 75), (125, 75), 0, fill = True)
bf.roundrect(55, 60, 40, 65, 5, 0, fill = True)
bf.draw_text(75, 20, "TOP", 0, align = CENTER)
bf.draw_text(75, 145, "BOTTOM", 0, align = CENTER)

tg = dpio.TileGrid(bmp, pixel_shader = pal)
g = dpio.Group()
g.append(tg)

disp = board.DISPLAY
disp.show(g)

mv = MotionEvents()
be = ButtonEvents()

def update() :
    (x, y, _) = mv.acc.acceleration
    th = math.atan2(y, x)
    bmp.fill(0)
    bmt.rotozoom(bmp, src, ox = 160, oy = 120, px = 75, py = 75, angle = th)

while be.buttons() == 0 :
    update()

mv.deinit()
