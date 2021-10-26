import displayio as dpio
from RictyKanji import draw_char, set_palette, han2zen
import time
import bitmaptools as bmt

class KanjiTerminal(dpio.Group) :
    def __init__(self, width, height, scroll = 1) :
        """Set up Kanji terminal of (width, height) size.  Number of scroll
        lines at a time can be specified.  A Hankaku-character is
        displayed in Zenkaku.

        """
        super().__init__()
        self.bmp = dpio.Bitmap(width << 4, height << 4, 4)
        self.pal = dpio.Palette(4)
        set_palette(self.pal)
        self.tg  = dpio.TileGrid(self.bmp, pixel_shader = self.pal)
        self.width  = width
        self.height = height
        self.scroll = max(1, min(height-1, scroll))
        self.delay  = None			# scroll delay
        self.curs_x = 0
        self.curs_y = 0
        self.append(self.tg)
        
    def cls(self) :
        """Clear whole screen and move cursor at (0, 0)."""
        
        self.bmp.fill(0)
        self.curs_x = 0
        self.curs_y = 0
        
    def locate(self, x, y) :
        """Move cursor to (x, y) position."""
        self.curs_x = max(0, min(x, self.width -1))
        self.curs_y = max(0, min(y, self.height -1))

    def vscroll(self, n = None) :
        """Scroll up n lines"""
        if n is None : n = self.scroll
        self.curs_y = max(0, self.curs_y - n)
        n <<= 4
        bmp = self.bmp
        bmp.blit(0, 0, bmp, x1 = 0, y1 = n, x2 = bmp.width, y2 = bmp.height)
        bmt.fill_region(bmp, 0, bmp.height - n, bmp.width, bmp.height, 0)
                
    def print(self, txt, delay = 0) :
        for c in han2zen(txt) :
            if self.curs_x >= self.width or c == "\n":
                self.curs_x = 0
                self.curs_y += 1
            if self.curs_y >= self.height :
                self.vscroll()
            if c != "\n" :
                draw_char(self.bmp, self.curs_x << 4, self.curs_y << 4, c)
                self.curs_x += 1
            time.sleep(delay)
