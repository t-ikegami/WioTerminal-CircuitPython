import board
import displayio as dpio
import analogio  as aio
import digitalio as dio
import rtc
import time
from NixieDisplay import NixieDisplay
from ButtonEvents import ButtonEvents
from MotionEvents import MotionEvents

disp = board.DISPLAY
g = dpio.Group()
ndp = NixieDisplay(5, 2)
g.append(ndp)

clock = rtc.RTC()
light = aio.AnalogIn(board.LIGHT)

def main() :
    mode = 1
    disp.auto_refresh = False		# this breaks time.sleep()??
    disp.show(g)
    be = ButtonEvents()
    me = MotionEvents() 

    def set_date_time(mon, day, hour, min) :
        disp.auto_refresh = True
        bmp = dpio.Bitmap(128, 120, 2)
        pal = dpio.Palette(2)
        pal.make_transparent(0)
        pal[1] = 0xFFFF00
        for x in range(128) : bmp[x, 0] = bmp[x, 119] = 1
        for y in range(120) : bmp[0, y] = bmp[127, y] = 1
        tg = dpio.TileGrid(bmp, pixel_shader = pal)
        g.append(tg)

        ndp.set_value(mon,  2, 0, 0, zp = False)
        ndp.set_value(day,  2, 3, 0, zp = False)
        ndp.set_value(hour, 2, 0, 1, zp = False)
        ndp.set_value(min,  2, 3, 1)
        ndp[2, 1] = 10
        tg.x = 0
        tg.y = 0
        while True:
            time.sleep(0.02)
            b = be.keys()
            if b == 0 : continue

            delta = 0
            if b & be.K_SELECT : break
            if b & be.K_UP    and tg.y > 0   : tg.y = 0
            if b & be.K_DOWN  and tg.y < 120 : tg.y = 120
            if b & be.K_LEFT  and tg.x > 0   : tg.x = 0
            if b & be.K_RIGHT and tg.x < 192 : tg.x = 192
            if b & be.K_O     : delta = +1
            if b & be.K_START : delta = -1

            if tg.x == 0 and tg.y == 0 :
                mon  = (mon - 1 + delta) % 12 + 1
                ndp.set_value(mon,  2, 0, 0, zp = False)
            if tg.x > 0  and tg.y == 0 :
                day  = (day - 1 + delta) % 31 + 1
                ndp.set_value(day,  2, 3, 0, zp = False)
            if tg.x == 0 and tg.y > 0  :
                hour = (hour + delta) % 24
                ndp.set_value(hour, 2, 0, 1, zp = False)
            if tg.x > 0  and tg.y > 0  :
                min  = (min + delta) % 60
                ndp.set_value(min,  2, 3, 1)

        clock.datetime = time.struct_time((2021, mon, day, hour, min, 0, -1, -1, -1))
        g.pop()
        disp.auto_refresh = False
        
    while True:
        m = me.motion()
        if   m & me.M_HEAD_UP   : disp.rotation = 0
        elif m & me.M_HEAD_DOWN : disp.rotation = 180

        b = be.buttons()
        if   b & be.K_SELECT : break
        elif b & be.K_X :
            mode = (mode + 1) % 3
            ndp.fill(11)
        elif b & be.K_O :
            ndp.fill(11)
            ts = clock.datetime
            set_date_time(ts.tm_mon, ts.tm_mday, ts.tm_hour, ts.tm_min)
            mode = 1
            
        if mode == 2 :
            v = light.value
            ndp.set_value(v, 5, 0, 0, zp = False)
            ndp.set_value(int(v * light.reference_voltage / 65535 * 100), 5, 0, 1, zp = False)
        else :
            ts = clock.datetime
            ndp.set_value(ts.tm_hour, 2, 0, mode, zp = False)
            ndp.set_value(ts.tm_min,  2, 3, mode)
            ndp[2, mode] = 10 + (ts.tm_sec & 1)

            if mode == 0 :
                ndp.set_value(ts.tm_sec,  2, 3, 1)
            else :
                ndp.set_value(ts.tm_mon,  2, 0, 0, zp = False)
                ndp.set_value(ts.tm_mday, 2, 3, 0, zp = False)

                if mode == 3 :
                    set_date_time(ts.tm_mon, ts.tm_mday, ts.tm_hour, ts.tm_min)
        
        disp.refresh()
        time.sleep(0.1)

    be.deinit()
    me.deinit()
    disp.show(None)
    disp.auto_refresh = True
    disp.rotation = 0
    
main()
