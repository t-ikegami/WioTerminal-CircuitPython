import board
import displayio as dpio
import terminalio as tio
import time
import uzlib
from ButtonEvents import ButtonEvents

bmp = dpio.Bitmap(475, 12, 2)
for i in range(95) :
    bmp.blit(i * 5, 0, tio.FONT.bitmap, x1 = i * 6, y1 = 2, x2 = i * 6 + 5, y2 = 14)
pal = dpio.Palette(2)
pal[1] = 0xFFFFFF
tg = dpio.TileGrid( bmp, pixel_shader = pal, width = 64, height = 14,
                    tile_width = 5, tile_height = 12 )

disp = board.DISPLAY
g = dpio.Group()
g.append(tg)
g.y = 40
disp.show(g)
be = ButtonEvents()

term = tio.Terminal(tg, tio.FONT)

disp.auto_refresh = False
with open("sw1.txt.gz", "rb") as f :
    dec = uzlib.DecompIO(f, 31)
    while True :
        key = be.get_pressed()
        if key & be.K_SELECT : break
        if key & be.K_X :
            for i in range(14 * 10) : dec.readline()
        if key & be.K_RIGHT :
            for i in range(14 * 100) : dec.readline()
        l = dec.readline()
        if not l : break
        delay = int(l)
        term.write("\x1b[2J")
        for i in range(1, 14) :
            term.write(f"\x1b[{i};1H")
            term.write(dec.readline()[1:65])
        disp.refresh()
        if delay > 2 and key == 0: time.sleep(delay / 15)

    disp.auto_refresh = True

