import ugame
import stage
from random import randrange
from micropython import const

VMAX   = const(4)
XMAX   = const(320)
YMAX   = const(240)
VRANGE = (VMAX << 9)
VZERO  = VRANGE >> 1

class Ball(stage.Sprite):
    def __init__(self) :
        self.cx = randrange(XMAX - 16)
        self.cy = randrange(YMAX - 16)
        self.dx = self.dy = VZERO
        while abs(self.dx - VZERO) < 128 :
            self.dx = randrange(VRANGE)
        while abs(self.dy - VZERO) < 128 :
            self.dy = randrange(VRANGE)
        self.ex = 0
        self.ey = 0
        self.col = 1 + randrange(3)*4
        self.delta = 0
        
        super().__init__(bank, randrange(4) + self.col, self.cx, self.cy)
        self.imune = set()

    def update(self):
        self.ex += self.dx
        self.ey += self.dy
        dx = (self.ex >> 8) - VMAX
        dy = (self.ey >> 8) - VMAX
        self.cx += dx
        self.cy += dy
        self.delta += abs(dx) + abs(dy)
        self.ex &= 0xFF
        self.ey &= 0xFF

        if self.cx < 0 :
            self.cx = 0
            self.ex = 0
            if self.dx < VZERO : self.dx = VRANGE - self.dx
            self.imune.clear()
        if self.cx > XMAX - 16 :
            self.cx = XMAX - 16
            self.ex = 0
            if self.dx > VZERO : self.dx = VRANGE - self.dx
            self.imune.clear()
        if self.cy < 0 :
            self.cy = 0
            self.ey = 0
            if self.dy < VZERO : self.dy = VRANGE - self.dy
            self.imune.clear()
        if self.cy > YMAX - 16 :
            self.cy = YMAX - 16
            self.ey = 0
            if self.dy > VZERO : self.dy = VRANGE - self.dy
            self.imune.clear()

        super().update()
        if self.delta > 4 :
            self.set_frame(self.frame % 4 + self.col)
            self.delta = 0
        self.move(self.cx, self.cy)
        
bank = stage.Bank.from_bmp16("ball.bmp")
background = stage.Grid(bank, XMAX//16, YMAX//16)

n = 15
balls = [ Ball() for i in range(n) ]

game = stage.Stage(ugame.display, 24, 1)
game.layers = balls + [background]
game.render_block()

while not ugame.buttons.get_pressed() :
    for ball in balls: ball.update()
    
    for i in range(1, n) :
        b = balls[i]
        for j in range(i) :
            c = balls[j]
            if (j in b.imune) and (i in c.imune) : continue

            dx = ((c.cx << 8) + c.ex) - ((b.cx << 8) + b.ex)
            dy = ((c.cy << 8) + c.ey) - ((b.cy << 8) + b.ey)
            if abs(dx) >= (16 << 8) or abs(dy) >= (16 << 8) : continue
            
            dd = dx*dx + dy*dy
            if dd >= (16 << 8) * (16 << 8) : continue
            
            wv = (c.dx * dx + c.dy * dy) - (b.dx * dx + b.dy * dy)
            wx = wv * dx // dd
            wy = wv * dy // dd
            b.dx += wx
            b.dy += wy
            c.dx -= wx
            c.dy -= wy
                
            b.imune.add(j)
            c.imune.add(i)
            
    game.render_sprites(balls)
    game.tick()
