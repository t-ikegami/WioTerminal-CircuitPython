import os
import board
import displayio as dpio
import mount_sd
from ButtonEvents import ButtonEvents
import time
from micropython import const
import gc

WIDTH  = const(320)
HEIGHT = const(240)
path   = "/sd/Pictures"

disp  = board.DISPLAY
g = dpio.Group()
disp.show(g)
be = ButtonEvents()

files = [ name for name in os.listdir(path) if name.endswith(".bmp") ]

disp.auto_refresh = False
idx = 0
while True :
    gc.collect()
    with open(f"{path}/{files[idx]}", "rb") as f :
        print(files[idx])
        image = dpio.OnDiskBitmap(f)
        tg = dpio.TileGrid(image, pixel_shader = image.pixel_shader)
        g.scale = max(1, min(WIDTH // image.width, HEIGHT // image.height))
        g.x = (WIDTH  - image.width  * g.scale) // 2
        g.y = (HEIGHT - image.height * g.scale) // 2
        g.append(tg)
        disp.refresh()

        count = 20	# 10 sec.
        while count > 0 :
            time.sleep(0.5)
            b = be.buttons()
            if b : break
            count -= 1

        if count == 0 : idx += 1
        elif b & be.K_SELECT :
            g.pop()
            break
        elif b & be.K_LEFT     : idx -= 1
        elif b & be.K_RIGHT    : idx += 1

        if idx < 0 : idx = len(files) - 1
        if idx >= len(files) : idx = 0

        g.pop()

disp.auto_refresh = True
be.deinit()
