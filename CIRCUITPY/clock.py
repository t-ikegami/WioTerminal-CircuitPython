import time
import board
import pwmio
from AnalogClock import Clock
from ButtonEvents import ButtonEvents

disp = board.DISPLAY
c = Clock(200)
c.x = 60
c.y = 20
disp.show(c)
disp.auto_refresh = False
be = ButtonEvents()

def set_alarm(alarm) :
    while be.keys() : pass	# wait for all buttons are released
    (switch, hour, min) = alarm

    def set_hand() :
        c.set_time(hour, min)
        if switch :
            c.hour.set_color(0xFF0000)
            c.min.set_color(0xFF0000)
        disp.refresh()

    set_hand()
    
    while True :
        time.sleep(0.05)
        b = be.keys()
        if b == 0 : continue

        if   b & be.K_O : break
        elif b & be.K_START :
            t = time.localtime()
            hour = t.tm_hour
            min  = t.tm_min
        elif b & be.K_UP     : min += 15
        elif b & be.K_DOWN   : min -= 15
        elif b & be.K_RIGHT  : min += 1
        elif b & be.K_LEFT   : min -= 1
        elif b & be.K_X	     :
            switch = not switch
            c.daytime = -1		# to reset the hand color

        if min >= 60 :
            min -= 60
            hour += 1
        if min < 0 :
            min += 60
            hour -= 1
        if hour >= 24 : hour -= 24
        if hour < 0   : hour += 24

        set_hand()

    c.daytime = -1			# to reset the hand color
    return (switch, hour, min)

alarm  = (False, 6, 0)
buzzer = None
count  = 0
t0     = None
while True :
    time.sleep(0.1)
    b = be.buttons()
    t = time.localtime()
    
    if buzzer is not None :
        # pppppp....pppppp....
        count += 1
        if count % 20 <= 12 :
            buzzer.duty_cycle = 0x8000 * (count & 1)
        if b or count >= 600 :
            buzzer.deinit()
            buzzer = None
            continue
    elif (True, t.tm_hour, t.tm_min) == alarm :
        if count == 0 :
            buzzer = pwmio.PWMOut(board.BUZZER, duty_cycle = 0, frequency = 880)
    else :
        count = 0
        
    if t == t0  and  b == 0 : continue
    
    c.set_time(t.tm_hour, t.tm_min, t.tm_sec)
    disp.refresh()

    if   b & be.K_SELECT : break
    elif b & be.K_O :
        alarm = set_alarm(alarm)
        count = 0

disp.auto_refresh = True    
be.deinit()



