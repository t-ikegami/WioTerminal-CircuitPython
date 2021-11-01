import os
import time
import board
import displayio as dpio
from AnalogClock import Clock
from ButtonEvents import ButtonEvents
import mount_sd

disp = board.DISPLAY
g = dpio.Group()

c = Clock(100)
c.x = 215
c.y = 5
c.face.pal.make_transparent(0)
g.append(c)

path   = "/sd/Pictures"
files = [ name for name in os.listdir(path) if name.endswith(".bmp") ]
idx = None
f   = None
bmp = None

def set_background(i) :
    global idx, f, bmp
    i %= len(files)
    if i == idx : return
    idx = i

    if f is not None :
        f.close()
        g.pop(0)

    f = open(f"{path}/{files[idx]}", "rb")
    bmp = dpio.OnDiskBitmap(f)
    tg  = dpio.TileGrid(bmp, pixel_shader = bmp.pixel_shader)
    g.insert(0, tg)

set_background(0)

disp.show(g)

be = ButtonEvents()
disp.auto_refresh = False
while True :
    ts = time.localtime()
    c.set_time(ts.tm_hour, ts.tm_min)
    disp.refresh()
    
    time.sleep(0.5)
    b = be.buttons()
    if b == 0 : continue
    if   b & be.K_SELECT : break
    elif b & be.K_X     : (c.x, c.y) = (110, 70)
    elif b & be.K_LEFT  : c.x = 5
    elif b & be.K_RIGHT : c.x = 215
    elif b & be.K_UP    : c.y = 5
    elif b & be.K_DOWN  : c.y = 135
    elif b & be.K_O     : set_background(idx + 1)
    elif b & be.K_START : set_background(idx - 1)

disp.auto_refresh = True    
be.deinit()
g.pop(0)
f.close()



