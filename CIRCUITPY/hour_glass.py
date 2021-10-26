import board
import time
from HourGlass import HourGlass
from ButtonEvents import ButtonEvents
from MotionEvents import MotionEvents

import displayio as dpio
import terminalio as tio

pal = dpio.Palette(2)
pal[1] = 0xFF8866
pal.make_transparent(0)
tg = dpio.TileGrid(tio.FONT.bitmap, pixel_shader = pal, 
                   width = 6, height = 1, tile_width = 6, tile_height = 14)
tg.transpose_xy = True
tg.flip_x = True
g = dpio.Group(scale = 2, x = 280, y = 75)
g.append(tg)
term = tio.Terminal(tg, tio.FONT)

disp = board.DISPLAY
hg = HourGlass(180)
hg.append(g)
disp.show(hg)
be = ButtonEvents()
me = MotionEvents()

t0 = None
while not be.get_pressed() :
    m = me.motion()
    if   m & me.M_LEFT_MID :
        hg.stop()
    elif m & me.M_LEFT_UP :
        if disp.rotation != 0 :
            disp.rotation = 0
            hg.t = hg.duration - hg.t
        hg.start()
    elif m & me.M_LEFT_DOWN :
        if disp.rotation != 180 :
            disp.rotation = 180
            hg.t = hg.duration - hg.t
        hg.start()
        
    if hg.is_stopped() :
        if t0 is None : t0 = time.time()
        if time.time() - t0 > 10 :
            disp.brightness = 0
    else :
        if t0 is not None :
            t0 = None
            disp.brightness = 1
            
        t = hg.duration - hg.t
        term.write("\r{:02d}:{:02d}".format(t // 60, t % 60))
        hg.tick()
        
    time.sleep(0.2)

be.deinit()
me.deinit()
disp.brightness = 1
disp.rotation = 0
