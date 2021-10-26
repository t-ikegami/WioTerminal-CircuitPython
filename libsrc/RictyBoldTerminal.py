import terminalio as tio
import displayio  as dpio
import adafruit_imageload as imgload

# tio.Terminal does not accept subclass of TileGrid, so we cannot maek TileGrid as a base class.
# Also, it seems not possible to subclass tio.Terminal.

class RictyTerminal (dpio.Group):
    Bitmap, Palette = imgload.load("font/RictyBold.bmp")

    def __init__(self, width, height) :
        super().__init__()
        self.tg = dpio.TileGrid(self.Bitmap, pixel_shader = self.Palette,
                                width = width, height = height,
                                tile_width = 10, tile_height = 20)
        self.term = tio.Terminal(self.tg, tio.FONT)
        self.append(self.tg)
        self.width  = width
        self.height = height

    def write(self, txt) :
        return self.term.write(txt)

class RictyHTerminal (dpio.Group):
    Bitmap, Palette = imgload.load("font/RictyBoldH.bmp")
    Table = dict(zip("　っまみむめもらりるれろ、ー。わ０１２３４５６７８９・！やゆよ？をがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ〜「ん」ゃゅょあいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ",
                     """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""))

    def __init__(self, width, height) :
        super().__init__()
        self.tg = dpio.TileGrid(self.Bitmap, pixel_shader = self.Palette,
                                width = width, height = height,
                                tile_width = 20, tile_height = 20)
        self.term = tio.Terminal(self.tg, tio.FONT)
        self.append(self.tg)
    
    def write(self, txt) :
        txt = "".join(self.Table.get(x, x) for x in txt)
        return self.term.write(txt)
        
