import board
import busio
import sdcardio
import storage
import digitalio

spi = None
sd  = None
vfs = None

path = "/sd"

det = digitalio.DigitalInOut(board.SD_DET)
det.switch_to_input(pull = digitalio.Pull.UP)	# det.value == False if sd card is inserted.

def mount() :
    global spi, sd, vfs
    if det.value is True : return None
    if spi is not None : return False

    spi = busio.SPI(board.SD_SCK, MOSI = board.SD_MOSI, MISO = board.SD_MISO)
    sd  = sdcardio.SDCard(spi, board.SD_CS)
    vfs = storage.VfsFat(sd)
    storage.mount(vfs, path)
    return True

def umount() :
    global spi, sd, vfs
    if det.value is True : return None
    if spi is None : return False

    storage.umount(path)
    sd.deinit()
    spi.deinit()
    vfs = None
    sd  = None
    spi = None
    return True

def is_mounted() :
    if det.value is True : return None
    if spi is None : return False
    return True

mount()
