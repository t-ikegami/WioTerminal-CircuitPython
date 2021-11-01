import time
import array
import analogio as aio
import board
import gc
import microcontroller as mc
import ulab.numpy as np
from ulab.scipy.signal import spectrogram
from ButtonEvents import ButtonEvents
from BitmapFrameBuffer import BitmapFrameBuffer, CENTER
import displayio as dpio
import bitmaptools as bmt

bmp = dpio.Bitmap(320, 220, 2)
pal = dpio.Palette(2)
pal[1] = 0xFFFFFF
tg = dpio.TileGrid(bmp, pixel_shader = pal)

bmp_txt = dpio.Bitmap(320, 20, 2)
tg_txt = dpio.TileGrid(bmp_txt, pixel_shader = pal, x = 0, y = 220)
bf = BitmapFrameBuffer(bmp_txt, pal)
bf.draw_text( 50, 17,  "500", 1, align = CENTER)
bf.draw_text(100, 17, "1000", 1, align = CENTER)
bf.draw_text(150, 17, "1500", 1, align = CENTER)
bf.draw_text(200, 17, "2000", 1, align = CENTER)
bf.draw_text(250, 17, "2500", 1, align = CENTER)
bf.draw_text(300, 17, "3000", 1, align = CENTER)
bf.hline(0, 0, 320, 1)

g = dpio.Group()
g.append(tg_txt)
g.append(tg)

disp = board.DISPLAY
disp.show(g)

m = aio.AnalogIn(board.MIC)
n = 1024
d = array.array("H", [0] * n)

spec_norm = 200 / 5e6	# full scale = amplitude 0.5V 

def get_spectrum() :
    r = range(n)
    gc.disable()
    mc.disable_interrupts()
    t0 = time.monotonic_ns()
    for i in r : 
      d[i] = m.value
      mc.delay_us(52)
    t1 = time.monotonic_ns()
    mc.enable_interrupts()
    gc.enable()

    a = np.array(d)
    b = spectrogram(a - np.mean(a))[0:320] * spec_norm
    return np.array(219 - np.clip(b, 0, 219), dtype = np.uint8)

be = ButtonEvents()
disp.auto_refresh = False

while True :
    if be.buttons() : break

    sp = get_spectrum()
    bmp.fill(0)
    for (i, x) in enumerate(sp) :
        bmt.draw_line(bmp, i, 219, i, x, 1)
    disp.refresh()

be.deinit()
disp.auto_refresh = True    
disp.show(None)
