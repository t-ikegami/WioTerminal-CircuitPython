import board
import displayio as dpio
import adafruit_imageload as imgload
from ButtonEvents import ButtonEvents
import asyncio

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
freq = 1

async def blink() :
    # br = (0x05, 0x0F)
    br = ( 5, 6, 7, 8, 9, 11, 13, 15, 15, 13, 11, 9, 8, 7, 6, 5 )
    n  = len(br)
    
    while True :
        for b in br:
            cb = color_base(col)
            pal[0] = cb * 0x08
            pal[1] = cb * b
            await asyncio.sleep(freq / n)

async def main() :
    global col, freq

    t = asyncio.create_task(blink())
    be = ButtonEvents()
    
    while True:
        await asyncio.sleep(0.05)
        key = be.get_pressed()
        if   key == 0 : continue
        elif key & be.K_SELECT :
            break
        elif key & be.K_RIGHT :
            col += 1
            if col >= 8 : col = 1
        elif key & be.K_LEFT :
            col -= 1
            if col <= 0 : col = 7
        elif key & be.K_UP :
            freq -= 0.2
            if freq < 0.2 : freq = 0.2
        elif key & be.K_DOWN :
            freq += 0.2
            if freq > 2 : freq = 2

    t.cancel()
    be.deinit()

asyncio.run(main())
