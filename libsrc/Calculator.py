from Qnum import Qnum

NEW = 0
NUM = 1
DOT = 2

class Calculator :
    
    def __init__(self) :
        self.x = Qnum(0)
        self.y = Qnum(0)
        self.m = Qnum(0)
        self.mode = NEW
        self.op  = None
        self.eq_op = None

    def event(self, ev) :
        if   ev == "C" : self.event_clear()
        elif self.x.a is None : return
        elif "0" <= ev <= "9" : self.event_number(ev)
        elif ev == "." : self.event_dot()
        elif ev == "=" : self.event_equal()
        elif ev == "M" : self.event_memory()
        elif ev in "*/-+" : self.event_op(ev)
        elif ev in "RPpscter" : self.event_uop(ev)
        else :
            raise TypeError("Unknown event: " + ev)

    def event_number(self, ev) :
        if self.mode == NEW :
            self.x = Qnum(0)
            self.mode = NUM
        self.x.a = self.x.a * 10 + int(ev)
        if self.mode == DOT : self.x.b *= 10

    def event_dot(self) :
        if self.mode == NEW : self.x = Qnum(0)
        self.mode = DOT

    def do_calc(self, op) :
        if op is None : return
        elif op == "*" : self.x = self.y * self.x
        elif op == "/" : self.x = self.y / self.x
        elif op == "-" : self.x = self.y - self.x
        elif op == "+" : self.x = self.y + self.x
        
    def event_equal(self) :
        self.op = None
        self.do_calc(self.eq_op)
        self.mode = NEW
        self.output()

    def event_clear(self) :
        if self.x.a == 0 :	# All clear if second press of "C"
            self.op = self.eq_op = None
        else :
            self.x = Qnum(0)
        self.mode = NEW

    def event_memory(self) :
        self.m = +self.x	# copy
        
    def event_op(self, ev) :
        self.do_calc(self.op)
        self.mode = NEW
        self.y = self.x
        self.op = self.eq_op = ev

    def event_uop(self, ev) :
        if   ev == "p" :
            self.x = - self.x
            return
        elif ev == "R" : self.x = self.m
        elif ev == "P" : self.x = Qnum.pi
        elif ev == "p" : self.x = - self.x
        elif ev == "s" : self.x = self.x.sin()
        elif ev == "c" : self.x = self.x.cos()
        elif ev == "t" : self.x = self.x.tan()
        elif ev == "e" : self.x = self.x.exp()
        elif ev == "l" : self.x = self.x.log()
        elif ev == "r" : self.x = self.x.sqrt()
        self.mode = NEW
        self.output()
        
    def output(self) :
        x = str(self.x).rstrip("0").lstrip("+")
        print(x)
            
if __name__ == "__main__" :
    c = Calculator()
    for x in "123+456=123.456+111.111=256r=" : c.event(x)
    print()
    for x in "CP/3=+0=s0=c0=t" : c.event(x)
    print()
    for x in "CP/3=MsRcRt" : c.event(x)
    print()
    for x in "3.14M1592+0=R" : c.event(x)
