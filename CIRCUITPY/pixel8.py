import board
import displayio as dpio
from PixelDisplay import PixelDisplay, PixelThumb

disp = board.DISPLAY
g = dpio.Group()
disp.show(g)

pix = PixelDisplay(8, 8)
pix.scale = 2
pix.x = 20
pix.y = 40
g.append(pix)

thumb = PixelThumb(8, 8, 5, 10)
thumb.scale = 2
thumb.x = 200
thumb.y = 20
g.append(thumb)

with open("pixel8.dat", "r") as f :
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



