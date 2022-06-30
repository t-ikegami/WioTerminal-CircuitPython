import time
import ulab.numpy as np
import board
import analogio as aio
import displayio as dpio
from BitmapFrameBuffer import setup_framebuffer
from ButtonEvents import ButtonEvents

# setup drawboard
N = 8		# number of frames
bf = setup_framebuffer(80*N, 80, 4)
bf.set_palette(0, 0x000000, "Black")
bf.set_palette(1, 0xFF0000, "Red")
bf.set_palette(2, 0xFFBBCC, "Pink")
bf.set_palette(3, 0xFFFF00, "Yellow")


# draw pinwheel
bf.rect(40, 40-16, 20, 17, bf.Red, fill = True)
bf.circle(40+20, 40, 16, bf.Pink, fill = True)
bf.rect(40, 41, 40, 40, 0, fill = True)
bf.rect(40+20, 0, 40, 41, 0, fill = True)
bf.triangle((40+20, 40), (40+20, 40-16), (40+38, 40), bf.Pink, fill = True)
bf.rotozoom(bf.bmp, ox = 40, oy = 40, px = 40, py = 39,
            source_clip0 = (40, 40), source_clip1 = (79, 40-17), angle = np.pi,    skip_index = 0)
bf.rotozoom(bf.bmp, ox = 40, oy = 40, px = 40, py = 40,
            source_clip0 = (40, 40), source_clip1 = (79, 40-17), angle = np.pi/2,  skip_index = 0)
bf.rotozoom(bf.bmp, ox = 40, oy = 40, px = 40, py = 40,
            source_clip0 = (40, 40), source_clip1 = (79, 40-17), angle = -np.pi/2, skip_index = 0)
bf.circle(40, 40, 3, bf.Yellow, fill = True)

# copy & rotate pinwheels
for i in range(1, N) :
    bf.rotozoom(bf.bmp, ox = 40 + i*80, oy = 40, px = 40, py = 40,
              source_clip0 = (0, 0), source_clip1 = (80, 80), angle = np.pi*i/(N*2), skip_index = 0)

# setup display
tg = dpio.TileGrid(bf.bmp, pixel_shader = bf.pal, tile_width = 80, tile_height = 80,
                   x = 120, y = 80)
g = dpio.Group()
g.append(tg)
disp = board.DISPLAY
disp.show(g)

# Rotate piwheel according to mic input
disp.auto_refresh = False
mic = aio.AnalogIn(board.MIC)
n = 64
buf = np.zeros(n, dtype = np.uint16)

be = ButtonEvents()
idx = 0
speed = 0
while not be.buttons() :
    disp.refresh()
    for i in range(n) : buf[i] = mic.value
    mag = (np.max(buf) - 20000) // 300		# -5 - 105 scale
    if speed < mag :
        speed += 10
    else :
        speed -= 1
    speed = min(100, max(0, speed))
    if speed == 0 :
        time.sleep(0.5)
        continue
    idx += 1
    if idx >= N : idx = 0
    tg[0] = idx
    time.sleep(0.5/speed - 0.005)

disp.auto_refresh = True
