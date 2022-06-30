# https://hackaday.io/project/184322-nixie-tubed-angle-gauge
import math
import time
import board
import displayio as dpio
from NixieDisplay import NixieDisplay
from MotionEvents import MotionEvents
from ButtonEvents import ButtonEvents

nd = NixieDisplay(3, 2)
nd.x = 64
me = MotionEvents()
be = ButtonEvents()

disp = board.DISPLAY
g = dpio.Group()
g.append(nd)
disp.show(g)

def angle(x, y) :
    return round(abs(math.atan2(y, x) / math.pi * 180))

def gleq(a, b) :
    delta = 1 if abs(a-b) < 10 else 10
    if a < b - 10 : return 10
    if a < b      : return 1
    if a > b + 10 : return -10
    if a > b      : return -1
    return 0

ay = 0
az = 0
while True :
    b = be.buttons()
    if b & be.K_SELECT : break

    a = me.acceleration
    delta = gleq(ay, angle(a[0], a[1]))
    if delta != 0 :
        ay += delta
        nd.set_value(ay, digit = 3, y = 0, zp = False)
    delta = gleq(az, angle(a[0], a[2]))
    if delta != 0 :
        az += delta
        nd.set_value(az, digit = 3, y = 1, zp = False)
    
    time.sleep(0.1)

disp.show(None)


