import time
import random
import board

# screen width & height
WIDTH  = 50
HEIGHT = 18

def put(x, y, str):
    print(f"\033[{y+1};{x+1}H{str}", end = "")

def clear():
    print("\033[2J")

class Pict :
    rev_tbl = {
        "("  : ")",
        ")"  : "(",
        "\\" : "/",
        "/"  : "\\",
    }
    
    def __init__(self, data) :
        self.data = data
        self.width  = len(data[0])
        self.height = len(data)

    def draw(self, x, y) :
        x0 = max(-x, 0)
        y0 = max(-y, 0)
        x1 = min(self.width,  WIDTH  - x)
        y1 = min(self.height, HEIGHT - y)
        if x0 >= x1 or y0 >= y1 : return
        x = max(x, 0)
        for iy in range(y0, y1) :
            put(x, y + iy, self.data[iy][x0:x1])

    def reverse(self) :
        self.data = [ "".join( self.rev_tbl.get(x, x) for x in reversed(y) )
                      for y in self.data ]

D51STR = Pict([
    r"      ====        ________                ___________ ",
    r"  _D _|  |_______/        \__I_I_____===__|_________| ",
    r"   |(_)---  |   H\________/ |   |        =|___ ___|   ",
    r"   /     |  |   H  |  |     |   |         ||_| |_||   ",
    r"  |      |  |   H  |__--------------------| [___] |   ",
    r"  | ________|___H__/__|_____/[][]~\_______|       |   ",
    r"  |/ |   |-----------I_____I [][] []  D   |=======|__ ",
])

D51WHL1 = Pict([
    r"__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__ ",
    r" |/-=|___|=    ||    ||    ||    |_____/~\___/        ",
    r"  \_/      \O=====O=====O=====O_/      \_/            ",
])

D51WHL2 = Pict([
    r"__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__ ",
    r" |/-=|___|=O=====O=====O=====O   |_____/~\___/        ",
    r"  \_/      \__/  \__/  \__/  \__/      \_/            ",
])

D51WHL3 = Pict([
    r"__/ =| o |=-O=====O=====O=====O \ ____Y___________|__ ",
    r" |/-=|___|=    ||    ||    ||    |_____/~\___/        ",
    r"  \_/      \__/  \__/  \__/  \__/      \_/            ",
])

D51WHL4 = Pict([
    r"__/ =| o |=-~O=====O=====O=====O\ ____Y___________|__ ",
    r" |/-=|___|=    ||    ||    ||    |_____/~\___/        ",
    r"  \_/      \__/  \__/  \__/  \__/      \_/            ",
])

D51WHL5 = Pict([
    r"__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__ ",
    r" |/-=|___|=   O=====O=====O=====O|_____/~\___/        ",
    r"  \_/      \__/  \__/  \__/  \__/      \_/            ",
])

D51WHL6 = Pict([
    r"__/ =| o |=-~~\  /~~\  /~~\  /~~\ ____Y___________|__ ",
    r" |/-=|___|=    ||    ||    ||    |_____/~\___/        ",
    r"  \_/      \_O=====O=====O=====O/      \_/            ",
])

D51WHL = [ D51WHL1, D51WHL2, D51WHL3, D51WHL4, D51WHL5, D51WHL6 ]

COAL = Pict([
    r"                              ",
    r"                              ",
    r"    _________________         ",
    r"   _|                \_____A  ",
    r" =|                        |  ",
    r" -|                        |  ",
    r"__|________________________|_ ",
    r"|__________________________|_ ",
    r"   |_D__D__D_|  |_D__D__D_|   ",
    r"    \_/   \_/    \_/   \_/    ",
])

width  = D51STR.width + COAL.width
height = D51STR.height + D51WHL[0].height
assert height == COAL.height

disp = board.DISPLAY
disp.auto_refresh = False

y0 = HEIGHT - height - 1	# bottom line is left blank
if random.randint(0, 1) == 1 :
    for x in range(WIDTH, -width-1, -1) :
        clear()
        D51STR.draw(x, y0)
        D51WHL[x % len(D51WHL)].draw(x, y0 + D51STR.height)
        COAL.draw(x + D51STR.width, y0)
        disp.refresh()
        time.sleep(0.02)
else :
    D51STR.reverse()
    for x in D51WHL : x.reverse()
    D51WHL.reverse()
    COAL.reverse()
    for x in range(-width, WIDTH + 1) :
        clear()
        COAL.draw(x, y0)
        D51STR.draw(x + COAL.width, y0)
        D51WHL[x % len(D51WHL)].draw(x + COAL.width, y0 + D51STR.height)
        disp.refresh()
        time.sleep(0.02)
        
disp.auto_refresh = True
