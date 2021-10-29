import board
import displayio as dpio
from PixelDisplay import PixelDisplay, PixelThumb

disp = board.DISPLAY
g = dpio.Group()
disp.show(g)

pix = PixelDisplay(11, 11)
pix.scale = 2
pix.x = 16
pix.y = 10
g.append(pix)

thumb = PixelThumb(11, 11, 2, 8)
thumb.scale = 2
thumb.x = 252
thumb.y = 10
g.append(thumb)

with open("pixel.dat", "r") as f :
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



