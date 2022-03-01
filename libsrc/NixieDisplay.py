import displayio as dpio
import adafruit_imageload as imgload

class NixieDisplay(dpio.TileGrid) :
    # Load image to memory, because OnDiskBitmap is slow.
    bmp, pal = imgload.load("nixie.bmp", bitmap = dpio.Bitmap, palette = dpio.Palette)
    
    def __init__(self, width = 5, height = 2) :
        super().__init__(self.bmp, pixel_shader = self.pal, width = width, height = height,
                         tile_width = 64, tile_height = 120, default_tile = 11)

    def set_value(self, value, digit = None, x = 0, y = None, zp = True) :
        idx = x if y is None else x + y * self.width
        if digit is None : digit = self.width * self.height - idx
        for i in range(idx + digit -1, idx -1, -1) :
            if value < 0 :
                self[i] = 11
                continue
            self[i] = value % 10
            value //= 10
            if value == 0 and not zp : value = -1

    def fill(self, val) :
        for i in range(self.width * self.height) : self[i] = val

