import time
import board
import displayio as dpio
from random import randint
from adafruit_miniqr import QRCode
from ButtonEvents import ButtonEvents

# QRCode
# https://www.keyence.co.jp/ss/products/autoid/codereader/basic2d-qr-types.jsp
# The size of qr_type 2 is 25x25, and up to 32 bytes can be embedded with ECC = L.
# Up to qr_type = 9 seems to be supported. (53x53, 230 bytes)

bmp = dpio.Bitmap(25, 25, 2)
pal = dpio.Palette(2)
pal[0] = 0x000000
pal[1] = 0xFFFFFF
tg = dpio.TileGrid(bmp, pixel_shader = pal)

disp = board.DISPLAY
g = dpio.Group(scale = 8)
g.append(tg)
g.x = 60
g.y = 20
disp.show(g)

be = ButtonEvents()
disp.auto_refresh = False
t0 = None
while True :
    time.sleep(0.1)
    b = be.buttons()
    t = time.localtime()
    if t == t0 and b == 0 : continue

    if b & be.K_SELECT : break

    qr = QRCode(qr_type = 2)
    qr.add_data(f"{t.tm_year:02d}/{t.tm_mon:02d}/{t.tm_mday:02d} "
                f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}".encode())
    qr.make(mask_pattern = randint(0, 7))
    m = qr.matrix
    for y in range(25) :
        for x in range(25) :
            bmp[x, y] = bool(m[x, y])

    disp.refresh()
    t0 = t

be.deinit()
disp.auto_refresh = True
disp.show(None)
