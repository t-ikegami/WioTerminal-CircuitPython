import time, math
from micropython import const
import displayio as dpio
import vectorio as vio
import ulab.numpy as np
from BitmapFrameBuffer import BitmapFrameBuffer, CENTER, RIGHT

ARM_LENGTH = const(110)
ARM_WIDTH  = const(5)
RADIAN = 0.0174532925

class Meter (dpio.Group):
    def __init__(self, vmin = 0, vmax = 100, title = "METER", size = 1.3333) :
        super().__init__()
        self.vmin = vmin
        self.vmax = vmax
        self.size = size
        self.append(self.face(title))

        needpl = dpio.Palette(1)
        needpl[0] = 0xFF0000
        self.needle = vio.Polygon(pixel_shader = needpl, points = [(0, 0), (0, 0), (0, 0)])
        self.append(self.needle)

        self.ox = int(size * 120)
        self.oy = int(size * (140 - 20))
        self.set_angle(-90)
        
    def face(self, title) :
        bitmap  = dpio.Bitmap(int(self.size * 240), int(self.size * 126), 8)
        palette = dpio.Palette(8) 

        bf = BitmapFrameBuffer(bitmap, palette)
        bf.set_palette(0, 0x000000, "BLACK")
        bf.set_palette(1, 0xD0D0D0, "GRAY")
        bf.set_palette(2, 0x00FF00, "GREEN")
        bf.set_palette(5, 0xFFC000, "ORANGE")
        bf.set_palette(6, 0xFFFF00, "YELLOW")
        bf.set_palette(7, 0xFFFFFF, "WHITE")
        
        bf.fill(bf.GRAY)
        mx = int(5 * self.size)
        my = int(5 * self.size)
        bf.rect(mx, my, bf.width - (mx<<1), bf.height - (my<<1), bf.WHITE, fill = True)
        bf.rect(mx, my, bf.width - (mx<<1), bf.height - (my<<1), bf.BLACK)

        # Draw ticks every 5 degrees from -50 to +50 degrees (100 deg. FSD swing)
        tick = np.arange(-50., 51, 5)
        sx   = np.cos((tick - 90) * RADIAN)
        sy   = np.sin((tick - 90) * RADIAN)
        x0   = np.array(self.size * (sx * (100 +  0) + 120), dtype = np.int16)
        y0   = np.array(self.size * (sy * (100 +  0) + 140), dtype = np.int16)
        x1   = np.array(self.size * (sx * (100 + 15) + 120), dtype = np.int16)
        y1   = np.array(self.size * (sy * (100 + 15) + 140), dtype = np.int16)
        x2   = np.array(self.size * (sx * (100 +  8) + 120), dtype = np.int16)
        y2   = np.array(self.size * (sy * (100 +  8) + 140), dtype = np.int16)

        for idx, i in enumerate(range(-50, 51, 5)) :
            if   (i >= -50 and i <  0) : color = bf.GREEN
            elif (i >=   0 and i < 25) : color = bf.YELLOW
            elif (i >=  25 and i < 50) : color = bf.ORANGE

            if i < 50 :
                bf.triangle( (x0[idx], y0[idx]), (x1[idx], y1[idx]), (x1[idx+1], y1[idx+1]), color, fill = True)
                bf.triangle( (x0[idx], y0[idx]), (x0[idx+1], y0[idx+1]), (x1[idx+1], y1[idx+1]), color, fill = True)
                
            # Short scale tick length
            if (i % 25 == 0):
                bf.line(x0[idx], y0[idx], x1[idx], y1[idx], bf.BLACK)
            else :
                bf.line(x0[idx], y0[idx], x2[idx], y2[idx], bf.BLACK)

            # Check if labels should be drawn, with position tweaks
            if (i % 25 == 0):
                x = int(self.size * (sx[idx] * (100 + 15 + 10) + 120))
                y = int(self.size * (sy[idx] * (100 + 15 + 10) + 140))

                if(i/25 == -2 ):
                    bf.draw_text(x, y,     "0",   bf.BLACK, align = CENTER)
                elif (i/25 == -1 ):
                    bf.draw_text(x, y + 3, "25",  bf.BLACK, align = CENTER)
                elif (i/25 == -0 ):
                    bf.draw_text(x, y + 5, "50",  bf.BLACK, align = CENTER)
                elif (i/25 == 1 ):
                    bf.draw_text(x, y + 3, "75",  bf.BLACK, align = CENTER)
                elif (i/25 == 2 ): 
                    bf.draw_text(x, y,     "100", bf.BLACK, align = CENTER)
            
                # Now draw the arc of the scale
                # sx = math.cos((i + 5 - 90) * RADIAN)
                # sy = math.sin((i + 5 - 90) * RADIAN)
                # x0 = sx * self.size * 100 + self.size * 120
                # y0 = sy * self.size * 100 + self.size * 140
                # # Draw scale arc, don't draw the last part
                # if (i < 50):
                #     tft.drawLine(int(x0), int(y0), int(x1), int(y1), tft.color.BLACK)

        bf.draw_text(int(self.size * 230), int(self.size * 119), title, bf.BLACK, align = RIGHT)
        bf.draw_text(int(self.size * 120), int(self.size *  90), title, bf.BLACK, align = CENTER, size = 2)

        self.width  = bf.width
        self.height = bf.height
        return bf

    def set_angle(self, angle):
        # full-scale range: [-140, -40]
        
        # Calculate tip of needle coords
        sx = math.cos(angle * RADIAN)
        sy = math.sin(angle * RADIAN)

        # Calculate width of needle
        dx = int(self.size * (ARM_WIDTH / -sy ))

        # Calculate x delta of needle start (does not start at pivot point)
        tx = int(self.size * 20 * math.tan((angle + 90) * RADIAN))

        sx = int(self.size * (sx * ARM_LENGTH + 120))
        sy = int(self.size * (sy * ARM_LENGTH + 140))

        # Draw the needle
        self.needle.points = [ (self.ox+tx-dx, self.oy), (sx, sy), (self.ox+tx+dx, self.oy) ]

        self.angle = angle
    
    def set_value(self, value, delay = 0):
        # map value to [-140, -40] degree, with overshoot of 10 degree
        angle = int(-140 + 100 * ((value - self.vmin) / (self.vmax - self.vmin)))
        if angle < -150 : angle = -150
        if angle > -30  : angle = -30

        if angle == self.angle : return
        
        if delay == 0:
            self.set_angle(angle)
            return

        while(angle != self.angle):
            if (self.angle < angle):
                self.set_angle(self.angle + 1)
            else:
                self.set_angle(self.angle - 1)

            if abs(self.angle - angle) < 10 :
                delay += delay >> 2
            
            time.sleep(delay/1000)

if __name__ == "__main__" :

    import board            
    from analogio import AnalogIn
    light = AnalogIn(board.LIGHT)
    meter = Meter(500, 63000, "LIGHT")
    disp = board.DISPLAY
    disp.show(meter)

    value = light.value
    while True:
        value = value * 0.98 + light.value * 0.02
        # print(value)
        meter.set_value(value, 20)
