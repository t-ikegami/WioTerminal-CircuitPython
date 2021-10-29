import time
import displayio as dpio
from ButtonEvents import ButtonEvents

class Cursor (dpio.TileGrid) :
    """An overlay box cursor for selection on screen."""
    
    def __init__( self, width, height, x0y0 = None, x1y1 = None, dxdy = None,
                  initial = (0, 0), color = 0xFFFF00, events = None ) :
        """Create a box cursor of size (width, height).  Moving range of (the
        top-left corner of) the cursor is given by (x0,y0) - (x1,y1),
        which is the whole screen by default.  Moving step is (dx,dy),
        which is (width, height) by default.  Initial cursor position
        (as a unit of (dx,dy)) can be specified.  The color of the
        cursor is yellow (0xFFFF00) by default.  If events dictionoary
        is given, event ids returned by get_event() method ares
        translated accordingly.

        """
        bmp = dpio.Bitmap(width, height, 2)
        for i in range(width)  : bmp[i, 0] = bmp[i, height - 1] = 1
        for i in range(height) : bmp[0, i] = bmp[width - 1, i]  = 1
        
        pal = dpio.Palette(2)
        pal.make_transparent(0)
        pal[1] = color

        super().__init__(bmp, pixel_shader = pal)

        (self.x0, self.y0) = (0, 0)                      if x0y0 is None else x0y0
        (self.x1, self.y1) = (320 - width, 240 - height) if x1y1 is None else x1y1
        (self.dx, self.dy) = (width, height)             if dxdy is None else dxdy
        (self.cx, self.cy) = initial

        self.mx = (self.x1 - self.x0) // self.dx
        self.my = (self.y1 - self.y0) // self.dy
        
        self.locate(self.cx, self.cy)
        self.be = ButtonEvents()
        self.events = events

    def __del__(self) :
        self.be.deinit()

    def set_color(self, color) :
        """Set color of the cursor.  If color = True/False, the cursor is
        shown/hidden.

        """
        if   color is False : self.hidden = True
        elif color is True  : self.hidden = False
        else :
            self.hidden = False
            self.pixel_shader[1] = color
    
    def locate(self, x, y) :
        """Move curosr to (x,y) position by a unit of (dx,dy).  If (x,y) is
        outside of the moving range, it is normalized.

        """
        if x < 0 : x = 0
        if y < 0 : y = 0
        if x > self.mx : x = self.mx
        if y > self.my : y = self.my
        self.x = self.x0 + self.dx * x
        self.y = self.y0 + self.dy * y
        self.cx = x
        self.cy = y

    def get_event(self, motion = False, oob = False, null = False) :
        """Return cursor position (x,y) where the K_X button is pressed.  If
        top three buttons (K_SELECT, K_START, and K_O) are pressed,
        (None,0-3) are returned respectively.  If motion = True,
        motion event of (None,20) is returned when cursor is moved.
        If oob = True, out-of-bound event of (None,10..13) is
        returned; 10: move left bound, 11: move bottom bound, 12: move
        right bound, 13: move top bound.  If null = True, (None, 30)
        is returned if nothing happens.  When events dictionaly is
        passed on initialization, the event ids (x,y) is mapped on the
        dict to return the translated ids.  In this case, events not
        found in the dict is ignored.

        """
        be = self.be
        while True:
            time.sleep(0.05)
            buttons = be.keys()
            if buttons == 0  and  not null : continue

            (ox, oy) = (self.cx, self.cy)
            if buttons & be.K_LEFT   : self.cx -= 1
            if buttons & be.K_RIGHT  : self.cx += 1
            if buttons & be.K_UP     : self.cy -= 1
            if buttons & be.K_DOWN   : self.cy += 1

            ev = None
            if oob :		# Out-of-bound event
                if   self.cx < 0       : ev = (None, 10)
                elif self.cy > self.my : ev = (None, 11)
                elif self.cx > self.mx : ev = (None, 12)
                elif self.cy < 0       : ev = (None, 13)
                
            self.locate(self.cx, self.cy)		# (cx, cy) is fixed to normal region

            if motion and (ox, oy) != (self.cx, self.cy) : ev = (None, 20)

            if   buttons & be.K_X      : ev = (self.cx, self.cy)
            elif buttons & be.K_SELECT : ev = (None, 0)
            elif buttons & be.K_START  : ev = (None, 1)
            elif buttons & be.K_O      : ev = (None, 2)
            
            if ev is None :
                if null : ev = (None, 30)
                else    : continue
            if self.events is None : return ev
            if ev in self.events   : return self.events[ev]
