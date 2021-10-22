import time
import board
import displayio as dpio
import adafruit_imageload as imgload
from ButtonEvents import ButtonEvents

bmp, pal = imgload.load("LED.bmp")
pal.make_transparent(3)
tg = dpio.TileGrid(bmp, pixel_shader = pal)

disp = board.DISPLAY
g = dpio.Group()
g.append(tg)

g.x = 110
g.y = 40

disp.show(g)

def color_base(col) :
    return (0x110000 * ((col >> 2) & 0x01)) | (0x001100 * ((col >> 1) & 0x01)) |  (0x000011 * (col & 0x01))

col = 0x04
cb  = color_base(col)
pal[0] = cb * 0x08
pause = 0.5

be = ButtonEvents()

while True:
    key = be.get_pressed()
    if key & be.K_SELECT : break
    if key :
        if key & be.K_RIGHT :
            col += 1
            if col >= 8 : col = 1
            cb = color_base(col)
            pal[0] = cb * 0x08
        if key & be.K_LEFT :
            col -= 1
            if col <= 0 : col = 7
            cb = color_base(col)
            pal[0] = cb * 0x08
        if key & be.K_UP :
            pause -= 0.1
            if pause < 0.1 : pause = 0.1
        if key & be.K_DOWN :
            pause += 0.1
            if pause > 1 : pause = 1
        
    pal[1] = cb * 0x05
    time.sleep(pause)
    pal[1] = cb * 0x0F
    time.sleep(pause)
    
be.deinit()
