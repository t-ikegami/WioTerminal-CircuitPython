import board
import displayio as dpio
from PixelDisplay import PixelDisplay, PixelThumb

disp = board.DISPLAY
g = dpio.Group()
disp.show(g)

pix = PixelDisplay(16, 16)
pix.x = 5
pix.y = 40
g.append(pix)

thumb = PixelThumb(16, 16, 4, 4)
thumb.scale = 2
thumb.x = 170
thumb.y = 40
g.append(thumb)

with open("pixel16.dat", "r") as f :
    dat = eval("".join(f.readlines()))
assert len(dat) <= thumb.nx * thumb.ny
for i, d in enumerate(dat) :
    if d is not None : thumb.set(i % thumb.nx, i // thumb.nx, d)
while len(dat) < thumb.nx * thumb.ny : dat.append(None)

while True :
    d = pix.dump()
    x = thumb.edit(d)
    if x is None :
        break
    elif isinstance(x, tuple) :
        dat[x[0] + x[1] * thumb.nx] = d
    elif isinstance(x, bytearray) :
        pix.restore(x)
        pix.edit()
        
print(repr(dat))



