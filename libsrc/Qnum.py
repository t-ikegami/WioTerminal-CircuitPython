import math

class Qnum :
    #
    # Rational number: a/b
    #
    bit_len = 52
    digit   = len(str(1 << bit_len)) - 1 - 3		# -3 means 3 digits off
    digit10 = 10**digit
    
    form = "{}{:d}.{:0" + str(digit) + "d}"

    def __init__(self, a, b = None) :
        if b is not None :
            self.a = a
            self.b = b
            self.normalize()
        elif isinstance(a, int) :
            self.a = a
            self.b = 1
        elif isinstance(a, float) :	# FP32
            self.a = int(a * 2**23)
            self.b = 2**23
            self.normalize()

    def normalize(self) :
        if self.a is None :	# NaN
            self.b = 1
            return
        if self.a == 0 :	# Zero
            self.b = 1
            return
        if self.b == 0 :	# +Infty or -Infty
            self.a = 1 if self.a > 0 else -1
            return
        if self.b < 0 : (self.a, self.b) = (-self.a, -self.b)
        (a, b) = (abs(self.a), self.b)
        alen = a.bit_length()
        blen = b.bit_length()
        bit = max( min(alen, blen) - self.bit_len,
                   max(alen, blen) - (self.bit_len << 1) )
        if bit > 0 :
            a >>= bit
            b >>= bit
        (self.a, self.b) = (a if self.a > 0 else -a, b)

    def __repr__(self) :
        return f"Qnum({self.a}, {self.b})"

    def __str__(self) :
        if self.a is None : return "Error"
        a = abs(self.a)
        if self.b == 0 : return "Infty" if self.a >= 0 else "-Infty"
        h = a * self.digit10 * 1000 // self.b
        (h, l) = divmod(h, 1000)
        if l > 500 : h += 1
        (h, l) = divmod(h, self.digit10)
        if h > self.digit10 : return "Infty" if self.a >= 0 else "-Infty"
        sign = "-" if self.a < 0 else "+"
        return self.form.format(sign, h, l)[:self.digit + 2]
    
    def __neg__(self) :
        return Qnum(-self.a, self.b)
        
    def __pos__(self) :
        return Qnum(self.a, self.b)
        
    def __add__(self, x) :
        if not isinstance(x, Qnum) : x = Qnum(x)
        return Qnum(self.a * x.b + self.b * x.a, self.b * x.b)

    def __sub__(self, x) :
        if not isinstance(x, Qnum) : x = Qnum(x)
        return Qnum(self.a * x.b - self.b * x.a, self.b * x.b)

    def __mul__(self, x) :
        if not isinstance(x, Qnum) : x = Qnum(x)
        return Qnum(self.a * x.a, self.b * x.b)

    def __truediv__(self, x) :
        if not isinstance(x, Qnum) : x = Qnum(x)
        return Qnum(self.a * x.b, self.b * x.a)

    def __radd__(self, x) :
        return self.__add__(x)

    def __rsub__(self, x) :
        return Qnum(x).__sub__(self)

    def __rmul__(self, x) :
        return self.__mul__(x)

    def __rtruediv__(self, x) :
        return Qnum(x).__truediv__(self)

    def sqrt(self) :
        if self.a < 0 : return Qnum.NaN
        x = Qnum(math.sqrt(self.a / self.b))
        (s0, s1) = ("", str(x))
        while s0 != s1 :
            x -= (x * x - self) / (x * 2)
            (s0, s1) = (s1, str(x))
        return x

    def exp(self) :
        s = +self if self.a > 0 else -self
        n = s.a // s.b
        s -= n
        x = Qnum(1)
        a = Qnum(1)
        b = 1
        c = 1
        (s0, s1) = ("", str(x))
        while s0 != s1 :
            a *= s
            b *= c
            c += 1
            x += a / b
            (s0, s1) = (s1, str(x))
        for _ in range(n) : x *= Qnum.e
        return x if self.a > 0 else 1/x

    def log(self) :
        if self.a < 0 : return Qnum.NaN
        n = self.a.bit_length() - self.b.bit_length()
        if n < 0 :
            a = self.a << (-n)
            b = self.b
        elif n > 0 :
            a = self.a
            b = self.b << n
        if a < b :
            a <<= 1
            n -= 1
        x = Qnum(a, b)
        x = (x-1)/(x+1)
        x2 = x * x
        a = x
        b  = 1
        (s0, s1) = ("", str(x))
        while s0 != s1 :
            a *= x2
            b += 2
            x += a / b
            (s0, s1) = (s1, str(x))
        return x * 2 + n * Qnum.log2

    def sin(self) :
        n = self / Qnum.pi
        n = n.a // n.b
        x = self - Qnum.pi * n
        x2 = x * x
        a = x
        b = 1
        c = 2
        (s0, s1) = ("", str(x))
        while s0 != s1 :
            a *= x2
            b *= - c * (c + 1)
            c += 2
            x += a / b
            (s0, s1) = (s1, str(x))
        return -x if n & 1 else x

    def cos(self) :
        self += Qnum.pi / 2
        return self.sin()

    def tan(self) :
        return self.sin() / self.cos()

Qnum.pi = Qnum(3141592653589793238462643383279,
               1000000000000000000000000000000)

Qnum.e  = Qnum(2718281828459045235360287471352,
               1000000000000000000000000000000)

Qnum.log2  = Qnum(6931471805599453094172321214581,
                 10000000000000000000000000000000)

Qnum.NaN = Qnum(None, 1)

Qnum.Infty = Qnum(1, 0)
 
