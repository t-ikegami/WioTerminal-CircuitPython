import board
import displayio as dpio
from BitmapFrameBuffer import BitmapFrameBuffer
import math
import time
from ButtonEvents import ButtonEvents

disp = board.DISPLAY
bitmap  = dpio.Bitmap(320, 240, 16)
palette = dpio.Palette(16) 

bf = BitmapFrameBuffer(bitmap, palette)
for i in range(16) :
    palette[i] = 0x111111 * i
palette.make_transparent(0)

g = dpio.Group()
g.append(bf)
disp.show(g)

cx = 40.0
cy = 40.0
c  = 1
th = 0.0

for r in range(40, 1, -1) :
    bf.circle(int(cx), int(cy), r, c, fill = True)
    bf.circle(int(cx) + 80, int(cy), r, 16 - c, fill = True)
    cx += 1.0 * math.cos(th)
    cy += 1.0 * math.sin(th)
    th += math.pi / 180.0 * 15.0
    c += 1
    if c > 15 : c = 1
    
bf.blit(  0, 160, bitmap, x1 = 0, y1 = 0, x2 = 80, y2 = 80)
bf.blit( 80,  80, bitmap, x1 = 0, y1 = 0, x2 = 80, y2 = 80)
bf.blit(160,   0, bitmap, x1 = 0, y1 = 0, x2 = 80, y2 = 80)
bf.blit(160, 160, bitmap, x1 = 0, y1 = 0, x2 = 80, y2 = 80)
bf.blit(240,  80, bitmap, x1 = 0, y1 = 0, x2 = 80, y2 = 80)

bf.blit(  0,  80, bitmap, x1 = 80, y1 = 0, x2 = 160, y2 = 80)
bf.blit( 80, 160, bitmap, x1 = 80, y1 = 0, x2 = 160, y2 = 80)
bf.blit(160,  80, bitmap, x1 = 80, y1 = 0, x2 = 160, y2 = 80)
bf.blit(240,   0, bitmap, x1 = 80, y1 = 0, x2 = 160, y2 = 80)
bf.blit(240, 160, bitmap, x1 = 80, y1 = 0, x2 = 160, y2 = 80)

be  = ButtonEvents()
while not be.get_pressed() :
    c = palette[1]
    for i in range(1, 15) : palette[i] = palette[i+1]
    palette[15] = c
    time.sleep(0.1)
