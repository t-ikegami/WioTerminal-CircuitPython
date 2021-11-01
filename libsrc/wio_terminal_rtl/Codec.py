import struct
# from micropython import const

# _VERSION = const(1)
_VERSION = 1

class Codec :
    # inp/out signatures are specified according to struct.pack/unpack
    # format.  "4H" like notation is not allowed, except for "4s", in
    # order to count the position in the parameter list. "I{}"
    # notation is used for string/binary, which is expanded like
    # "I16s" according to the length of the string. "b{}" notation is
    # used for nullable string/binary, which is expanded as either "b"
    # or "bI16s" depending on the null flag.  The out ends with "bxxs"
    # (with digit x) is treated specially: nullable structure is
    # expected as a return value.
    
    INP_HEADER = "<4BI"
    OUT_HEADER = "<8x"
    cache = {}
    serial = 0

    @classmethod
    def get_serial(cls) :
        cls.serial += 1
        return cls.serial

    @staticmethod
    def count_element(str) :
        return sum( not x.isdigit() for x in str )
    
    def __init__(self, sid, rid, typ, inp, out) :
        self.sid = sid
        self.rid = rid
        self.typ = typ
        self.inp = inp
        self.out = out
        if (sid, rid) not in self.cache :
            self.cache[(sid, rid)] = ( self.calc_inp_idx(), self.calc_out_idx() )
        (self.inp_idx, self.out_idx) = self.cache[(sid, rid)]

    def calc_inp_idx(self) :
        """Search "I{}" or "b{}" patterns in inp signature, and pre-calculate
        position in the parameter list."""

        sec = self.inp.split("{}")
        if len(sec) == 1 : return None
        sec.pop()
        if not all( x[-1] == "I" or x[-1] == "b" for x in sec ) :
            raise ValueError("Illegal input signature: " + self.inp)
        idx = [ self.count_element(x) for x in sec ]
        idx[0] -= 1
        for i in range(1, len(idx)) : idx[i] += idx[i-1]

        res = [ (s[-1] == "I", i) for s, i in zip(sec, idx) ]
        return tuple(reversed(res))

    def calc_out_idx(self) :
        """Search "I{}" or "b{}" patterns in out signature, and pre-calculate
        position in the buffer."""

        sec = self.out.split("{}")
        if len(sec) == 1 : return None
        last = sec.pop()
        if not all( x[-1] == "I" or x[-1] == "b" for x in sec ) :
            raise ValueError("Illegal output signature: " + self.out)
        nul = [ x[-1] == "I"          for x in sec ]
        idx = [ self.count_element(x) for x in sec ]
        idx[0] -= 1
        for i in range(1, len(idx)) : idx[i] += idx[i-1]
        loc = [ struct.calcsize("<" + x[:-1]) for x in sec ]

        # return value is nullable struct
        if ( len(last) >= 4 and
             last[-1] == "s" and last[-2].isdigit() and last[-3].isdigit() and last[-4] == "b" ) :
            nul.append(None)
            idx.append(idx[-1] + self.count_element(last[:-3]))
            loc.append(struct.calcsize("<" + last[:-4]))
                       
        return tuple(zip(nul, idx, loc))

    def pack(self, *param) :
        param = list(param)
        form = self.INP_HEADER + self.inp_format(param)
        return struct.pack( form,
                            self.typ, self.rid, self.sid, _VERSION,
                            self.get_serial(),
                            *param)

    def inp_format(self, param) :	# param is modified on return
        if self.inp_idx is None : return self.inp
        fill = []
        for (flag, idx) in self.inp_idx :
            if flag :  # "I{}"
                sz = len(param[idx])
                fill.insert(0, str(sz) + "s")
                param.insert(idx, sz)
            else :  # "b{}"
                if param[idx] is None :
                    fill.insert(0, "")
                    param[idx] = 1
                else :
                    sz = len(param[idx])
                    fill.insert(0, "I" + str(sz) + "s")
                    param.insert(idx, sz)
                    param.insert(idx, 0)
        return self.inp.format(*fill)
        
    def unpack(self, buf) :
        form = self.OUT_HEADER + self.out_format(buf)
        param = list(struct.unpack(form, buf))
        self.out_postprocess(param)
        n = len(param)
        return None     if n == 0 \
          else param[0] if n == 1 \
          else tuple(param)

    def out_format(self, buf) :
        if self.out_idx is None : return self.out
        fill = []
        pos = 8		# skip header
        form = self.out

        for (flag, idx, loc) in self.out_idx :
            pos += loc
            if flag :  # "I{}"
                sz, = struct.unpack_from("<I", buf, pos)
                fill.append(str(sz) + "s")
                pos += 4 + sz
            elif flag is False :  # "b{}"
                nul, = struct.unpack_from("<b", buf, pos)
                if nul :
                    fill.append("")
                    pos += 1
                else :
                    sz, = struct.unpack_from("<I", buf, pos + 1)
                    fill.append("I" + str(sz) + "s")
                    pos += 5 + sz
            else :  # None means nullable struct return
                nul, = struct.unpack_from("<b", buf, pos)
                if nul : form = form[:-3]

        return form.format(*fill)

    def out_postprocess(self, param) :
        if self.out_idx is None : return
        for (flag, idx, loc) in self.out_idx :
            if flag :  # "I{}"
                del param[idx]
            else : # "b{}" or nullable struct return
                if param[idx] :
                    param[idx] = None
                else :
                    del param[idx]
                    del param[idx]

if __name__ == "__main__" :
    c = Codec(1, 1, 0, "BBHIb{}H8sI{}b{}Ib", "BBHIb{}H8sI{}b{}Ib16s")
    print(c.inp_idx)
    print(c.out_idx)

    p = c.pack(1, 2, 3, 4, None, 5, b'abcdefgh', b'ijklm', b'honjamaka', 6, 1)
    u = c.unpack(p)
    print(p)
    print(u)
