import time
import board
import displayio as dpio
import bitmaptools as bmt
from random import randint
from ButtonEvents import ButtonEvents

bmp = dpio.Bitmap(320, 240, 4)
pal = dpio.Palette(4)
pal[1] = 0xFFFF00
pal[2] = 0xFFA500
pal[3] = 0x00A5FF

class Qix :
    def __init__(self, n = 10, color = 1) :
        self.x0 = randint(0, 279)
        self.y0 = randint(0, 199)
        self.x1 = self.x0 + randint(0, 40)
        self.y1 = self.y0 + randint(0, 40)
        self.vx0 = randint(4, 10)
        self.vy0 = randint(4, 10)
        self.vx1 = randint(4, 10)
        self.vy1 = randint(4, 10)
        self.color = color
        self.queue = [ ( self.x0, self.y0, self.x1, self.y1 ) ] * n

    def update(self) :
        self.x0 += self.vx0
        self.y0 += self.vy0
        self.x1 += self.vx1
        self.y1 += self.vy1
    
        if self.x0 < 0 : self.vx0 = randint(4, 10)
        if self.y0 < 0 : self.vy0 = randint(4, 10)
        if self.x1 < 0 : self.vx1 = randint(4, 10)
        if self.y1 < 0 : self.vy1 = randint(4, 10)

        if self.x0 >= 320 : self.vx0 = -randint(4, 10)
        if self.y0 >= 240 : self.vy0 = -randint(4, 10)
        if self.x1 >= 320 : self.vx1 = -randint(4, 10)
        if self.y1 >= 240 : self.vy1 = -randint(4, 10)

        if self.x0 < self.x1 + 50 : self.vx0 += 1; self.vx1 -= 1
        if self.y0 < self.y1 + 50 : self.vy0 += 1; self.vy1 -= 1
        if self.x1 < self.x0 + 50 : self.vx1 += 1; self.vx0 -= 1
        if self.y1 < self.y0 + 50 : self.vy1 += 1; self.vy0 -= 1
    
        self.x0 = max(0, min(self.x0, 319))
        self.y0 = max(0, min(self.y0, 239))
        self.x1 = max(0, min(self.x1, 319))
        self.y1 = max(0, min(self.y1, 239))
    
        p = self.queue.pop()
        bmt.draw_line(bmp, *p, value = 0)
        p = (self.x0, self.y0, self.x1, self.y1)
        self.queue.insert(0, p)
        bmt.draw_line(bmp, *p, value = self.color)
        
q1 = Qix(randint(10, 20), 1)
q2 = Qix(randint(10, 20), 2)
q3 = Qix(randint(10, 20), 3)

disp = board.DISPLAY
g = dpio.Group()
tg = dpio.TileGrid(bmp, pixel_shader = pal)
g.append(tg)
disp.show(g)

be = ButtonEvents()
while True :
    time.sleep(0.05)
    b = be.buttons()
    if b != 0 : break

    q1.update()
    q2.update()
    q3.update()

be.deinit()
