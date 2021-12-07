import board
import pulseio as pio
import array
import time

# Only NEC format is supported.
# http://elm-chan.org/docs/ir_format.html

class IROut :
    def __init__(self, IR = board.IR, Tr = 562) :
        self.pl = pio.PulseOut(IR, frequency = 38000, duty_cycle = 21845)
        self.Tr  = Tr	# in us

    def deinit(self) :
        self.pl.deinit()
        
    def send(self, id, data) :
        if id.bit_length() <= 8 : id = ((0xFF - id) << 8) | id
        code = ((0xFF - data) << 24) | data << 16 | id

        T = self.Tr
        p = [ T * 16, T * 8 ]
        for i in range(32) :
            p.append(T)
            p.append(T * (3 if (code >> i) & 0x01 else 1))
        p.append(T)
        p = array.array("H", p)

        self.pl.send(p)

class IRIn :
    def __init__(self, IR = board.LIGHT, maxlen = 200) :
        self.pl = pio.PulseIn(IR, maxlen = maxlen, idle_state = False)

    def deinit(self) :
        self.pl.deinit()

    def recv(self) :
        p = self.ir_recv()
        if p is None : return None

        p = self.ir_normalize(p)
        return self.ir_decode(p)

    def ir_recv(self) :
        if len(self.pl) == 0 : return None

        time.sleep(0.1)
        pl = self.pl
        pl.pause()
        p = array.array("H", (pl[i] for i in range(len(pl))))
        pl.clear()
        pl.resume()

        if len(p) < 67 : return None
        return p

    def estimate_tr(self, p = None) :
        while p is None :
            p = self.ir_recv()
        return (p[0] + p[1]) // 24
    
    @staticmethod
    def ir_normalize(p) :
        # estimate Tr for the remote controller
        Tr = (p[0] + p[1]) // 24
        tr = Tr // 2

        # fix raise/fall delay of LIGHT sensor, and normalize to the Tr unit
        # returns list, because array.array does not support sparse slice like [::2].
        return [ (x + (200 if i & 1 else -200) + tr) // Tr for i, x in enumerate(p) ]

    @staticmethod
    def ir_decode(p) :
        # decode normalized signal series
        
        if len(p) < 67 or p[0] < p[1] or p[1] < 5 or any(x >= 2 for x in p[2:67:2]) :
            # raise ValueError("Failed to decode; may not be an NEC format.")
            return False

        p = p[3::2]
        code = []
        for i in range(0, 32, 8) :
            c = 0
            for j in range(8) :
                if p[i + j] >= 2 : c |= (1 << j)
            code.append(c)    

        id = code[0]
        if id != (0xFF - code[1]) : id = (code[1] << 8) | id
        data = code[2]
        if data != (0xFF - code[3]) :
            # raise ValueError("Failed to decode; may not be an NEC format.")
            return False

        return (id, data)
    
