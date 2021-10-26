import time
import displayio as dpio
import adafruit_imageload as imgload

class HourGlass (dpio.Group) :
    """HourGlass showing 0-60.  To flip the glass, use Display.rotation =
    180.

    """
    Glass = imgload.load("HG_Glass.bmp")
    Lower = imgload.load("HG_Lower.bmp")
    Upper = imgload.load("HG_Upper.bmp")
    Sand  = imgload.load("HG_Sand.bmp")
    Back  = ( dpio.Bitmap(8, 8, 2), dpio.Palette(2) )

    Glass[1].make_transparent(3)
    Lower[1].make_transparent(1)
    Upper[1].make_transparent(1)
    Sand[1].make_transparent(1)

    Glass[1][5] = 0x707070
    Back[1][0] = 0x505050
    Back[0].fill(0)

    def __init__(self, duration = 180) :
        super().__init__()

        def gen_tg(tpl, x, y) :
            tg = dpio.TileGrid(tpl[0], pixel_shader = tpl[1])
            tg.transpose_xy = True
            tg.x, tg.y = x, y
            return tg

        self.glass = gen_tg(self.Glass,   0,   0)
        self.lower = gen_tg(self.Lower, 260,  60)	# x -> 200
        self.upper = gen_tg(self.Upper,  80,  50)	# x -> 140
        self.sand  = gen_tg(self.Sand,  160, 112)
        self.backU = dpio.TileGrid(self.Back[0], pixel_shader = self.Back[1], width = 20, height = 30,
                                   x = 0, y = 0)
        self.backL = dpio.TileGrid(self.Back[0], pixel_shader = self.Back[1], width = 20, height = 30,
                                   x = 160, y = 0)
        self.append(self.backU)
        self.append(self.upper)
        self.append(self.backL)
        self.append(self.sand)
        self.append(self.lower)
        self.append(self.glass)

        self.duration = duration
        self.t0 = time.time()
        self._t = 0

        self.value = 0

    def set_value(self, val) :
        """Recommended val range : 0..60"""
        if self.value == val : return
        self.lower.x = 260 - val
        self.upper.x = 80  + val
        self.value = val
    
    def tick(self) :
        self.sand.flip_x = (True, False)[self.sand.flip_x]
        self.set_value(self.t * 60 // self.duration)
        if self.t >= self.duration :
            self.stop()
            self.t = self.duration

    def start(self) :
        if self.t0 is None and self.t < self.duration:
            self.t0 = time.time()
            self.sand.hidden  = False
            self.upper.hidden = False

    def stop(self) :
        if self.t0 is None : return
        self._t += time.time() - self.t0
        self.t0 = None
        self.sand.hidden = True
        if self.t >= self.duration :
            self.upper.hidden = True

    def reset(self) :
        self._t = 0
        if self.t0 is not None :
            self.t0 = time.time()

    def is_stopped(self) :
        return self.t0 is None
            
    @property
    def t(self) :
        if self.t0 is None: return self._t
        return self._t + time.time() - self.t0

    @t.setter
    def t(self, t) :
        self._t = t
        
