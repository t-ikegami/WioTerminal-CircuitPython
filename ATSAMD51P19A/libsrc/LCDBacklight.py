import board
from ATSAMD51P19A import GCLK, MCLK, EVSYS, PORT, TC3

# Use TC3 to set/clear PC05 pin via EVSYS
# Assumes that nobody uses TC3 and EVSYS

PORTC = PORT.GROUP[2]

def init() :
    if MCLK.APBBMASK.TC3 or MCLK.APBBMASK.EVSYS :
        raise RuntimeError("TC3 or EVSYS are already in use")

    board.DISPLAY.auto_brightness = False	# set to true by reset_display()
    
    GCLK.PCHCTRL[26].reg = 0x45			# TC3   <- GCLK[5] = 2 MHz
    MCLK.APBBMASK.TC3 = 1
    MCLK.APBBMASK.EVSYS = 1

    PORTC.EVCTRL.reg = 0xA5C5			# PC05, EV0->CLR, EV1->SET

    EVSYS.USER[1].reg = 1			# PORT_EV0 = channel 0
    EVSYS.USER[2].reg = 2			# PORT_EV1 = channel 1
    EVSYS.CHANNEL[0].CHANNEL.reg = 0x0253	# channel 0 = TC3_MC0, async
    EVSYS.CHANNEL[1].CHANNEL.reg = 0x0252	# channel 1 = TC3_OVF, async

    TC3.COUNT8.CTRLA.SWRST = 1
    while TC3.COUNT8.SYNCBUSY.reg : pass
    TC3.COUNT8.CTRLA.reg = 0x0214		# DIV4 = 500kHz / 256, SYNC=PRESC, COUNT8
    TC3.COUNT8.EVCTRL.reg = 0x1100		# MC0 & OVF
    TC3.COUNT8.PER = 0xFF
    TC3.COUNT8.CC[0] = 0xFF
    while TC3.COUNT8.SYNCBUSY.reg : pass
    TC3.COUNT8.CTRLA.ENABLE = 1
    while TC3.COUNT8.SYNCBUSY.reg : pass

def deinit() :
    if MCLK.APBBMASK.TC3 == 0 :
        raise RuntimeError("Already deinited.")
    TC3.COUNT8.CTRLA.SWRST = 1
    EVSYS.CTRLA.SWRST = 1
    PORTC.EVCTRL.reg = 0

    MCLK.APBBMASK.EVSYS = 0
    MCLK.APBBMASK.TC3 = 0
    GCLK.PCHCTRL[26].reg = 0

    PORTC.OUTSET = 0x20				# turn on the backlight

def brightness(b = None) :
    if b is None :
        return TC3.COUNT8.CC[0] / 255
    b = max(0, min(255, int(b * 255)))
    TC3.COUNT8.CC[0] = b
