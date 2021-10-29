import os
import time
import board
import displayio as dpio
from TinyCalendar import Calendar
from ButtonEvents import ButtonEvents
import mount_sd

disp = board.DISPLAY
g = dpio.Group()

c = Calendar()
c.x = 200
c.y = 0
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

set_background(6)
disp.show(g)
disp.refresh()

be = ButtonEvents()
disp.auto_refresh = False
while True :
    time.sleep(0.5)
    b = be.buttons()
    if b == 0 : continue
    
    if   b & be.K_SELECT : break
    elif b & be.K_X     : (c.x, c.y) = (100, 70)
    elif b & be.K_LEFT  : c.x = 0
    elif b & be.K_RIGHT : c.x = 200
    elif b & be.K_UP    : c.y = 0
    elif b & be.K_DOWN  : c.y = 140
    elif b & be.K_O     : set_background(idx + 1)
    elif b & be.K_START : set_background(idx - 1)

    c.show_calendar(time.localtime())
    disp.refresh()

disp.auto_refresh = True    
be.deinit()
g.pop(0)
f.close()



