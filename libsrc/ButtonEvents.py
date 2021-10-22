import board
import keypad
from usb_cdc import console

class EventsBase :
    """EventsBase class is a base class that serves a bit-pattern of
    pressed buttons.  The base class itself is not instanciable; the
    subclass should define pad_setup() class method, where pad class
    variable is set up as an appropriate keypad object.  This class
    returns a singleton-like object: multiple calls of EventsBase()
    return instances backed up by an identical pad object, and those
    instances are safely deinit()ed.

    """
    pad      = None
    count    = 0		# number of instances
    state    = 0		# currently pressed buttons
    press    = 0		# newly pressed buttons
    ev       = keypad.Event()
    repstate = None		# initialized in pad_setup() for inheritance to work

    repdelay  = 9
    repperiod = 2

    @classmethod
    def pad_init(cls) :
        if not hasattr(cls, "pad_setup") :
            raise TypeError("EventsBase base class cannot be instanciated.")
        cls.count += 1
        if cls.pad is not None : return
        assert cls.count == 1
        cls.pad_setup()
        cls.state = 0
        cls.repstates = bytearray(cls.pad.key_count)
            
    @classmethod
    def pad_free(cls) :
        cls.count -= 1
        if cls.count > 0 : return
        cls.pad.deinit()
        cls.pad = None

    @classmethod
    def set_const(cls, tags) :
        """Set up class variables listed in tags such that tags[i]==(1<<i)"""
        for i, tag in enumerate(tags) : setattr(cls, tag, 1 <<  i)
        
    @classmethod
    def _get_pressed(cls) :
        """Returns bitpattern of currently pressed buttons; i.e.,
        newly-pressed or kept-pressed buttons.

        """
        cls.press = 0
        while cls.pad.events.get_into(cls.ev) :
            if cls.ev.pressed :
                cls.state |= (1 << cls.ev.key_number)
                cls.press |= (1 << cls.ev.key_number)
            elif cls.ev.released :
                cls.state &= ~(1 << cls.ev.key_number)
            else :
                raise RuntimeError("keypad events of neither pressed nor released.")

        return cls.state | cls.press

    # To override get_pressed, super().get_pressed() does not work in micropython.
    # Use cls._get_pressed() instead.
    #
    get_pressed = _get_pressed
    
    @classmethod
    def reset(cls) :
        cls.pad.reset()
        cls.pad.events.clear()
        cls.state = 0
        # for i in range(len(cls.repstates)) : cls.repstates[i] = 0

    @classmethod
    def wait_released(cls) :
        cls.reset()
        while cls.get_pressed() : pass
    
    def keys(self):
        """Returns bitpattern of pressed buttons.  By calling the method
        periodically (with delay of ~0.05s), the event is repeated if
        buttons are kept pressed.

        """
        pressed = self.get_pressed()
        events = 0
        bit = 1
        for i, st in enumerate(self.repstates) :
            if pressed & bit:
                st += 1
                if st >= self.repdelay + self.repperiod:
                    st = self.repdelay
                if st == 1 or st == self.repdelay:
                    events |= bit
            else:
                st = 0
            self.repstates[i] = st
            bit <<= 1
        return events

    def buttons(self) :
        """Returns bitpattern of newly pressed buttons."""
        
        self.get_pressed()
        return self.press

    def __init__(self) :
        self.pad_init()
        self.deinited = False

    def deinit(self) :
        if self.deinited : raise RuntimeError("ButtonEvents is already deinited.")
        self.pad_free()
        self.deinited = True


class ButtonEvents (EventsBase) :
    """ButtonEvents serves a bit-pattern of pressed buttons.  A set of
    buttons are set up in pad_setup() class method.  It also scans
    console keyboard (via usb_cdc), when no button is active.

    """
    console.timeout = 0

    @classmethod
    def pad_setup(cls) :
        """Initialize pad class variable.  Buttons defined here (for Wio
        Terminal) are pulled-up externally.  On other boards,
        keypad.Keys() may have to be tuned.

        """
        buttons = [
            ( "K_X",      board.SWITCH_PRESS ),
            ( "K_DOWN",   board.SWITCH_DOWN ),
            ( "K_LEFT",   board.SWITCH_LEFT ),
            ( "K_RIGHT",  board.SWITCH_RIGHT ),
            ( "K_UP",     board.SWITCH_UP ),
            ( "K_O",      board.BUTTON_1 ),
            ( "K_START",  board.BUTTON_2 ),
            ( "K_SELECT", board.BUTTON_3 ),
        ]

        cls.set_const([ x[0] for x in buttons ])
        cls.pad = keypad.Keys([ x[1] for x in buttons ], value_when_pressed = False, pull = False)

    @classmethod
    def get_console(cls) :
        state = 0
        while c := console.read(1) :
            if   c == b"h" or c == b"\x02" : state |= cls.K_LEFT
            elif c == b"j" or c == b"\x0e" : state |= cls.K_DOWN
            elif c == b"k" or c == b"\x10" : state |= cls.K_UP
            elif c == b"l" or c == b"\x06" : state |= cls.K_RIGHT
            elif c == b" " or c == b"\r"   : state |= cls.K_X
            elif c == b"1" : state |= cls.K_SELECT
            elif c == b"2" : state |= cls.K_START
            elif c == b"3" : state |= cls.K_O
            
            elif c == b"\x1b" :
                c = console.read(2)
                if   c == b"[A" : state |= cls.K_UP
                elif c == b"[B" : state |= cls.K_DOWN
                elif c == b"[C" : state |= cls.K_RIGHT
                elif c == b"[D" : state |= cls.K_LEFT

        cls.press = state
        return state
        
    @classmethod
    def get_pressed(cls) :
        res = cls._get_pressed()
        if res == 0 : res = cls.get_console()
        return res
