import struct

# parse c-style strut and pack into python struct.
# struct can be nested.
# array of structure is not supported.
#
#    Struct.define( "ip_info", """
#    uint8[4] ip;
#    uint8[4] netmask;
#    uint8[4] gw;
#    """)
#
#    Struct.define( "network_info", """
#    char[6]	mac;
#    ip_info	ip_info;""" )
#
#    net = Struct("network_info")
#    ip_info = net.ip_info
#    ip_info.ip = (192, 168, 1, 1)
#    ip_info.netmask = (255, 255, 0, 0)
#    ip_info.gw = (192, 168, 1, 0)
#
#    net.mac = b'012345'
#
#    print(net.mac)
#    print(net.ip_info.ip)
#    print(net.ip_info)
#    print(net._data)

_type = { "bool"	: (1, "b"),
          "int8"	: (1, "b"),
          "uint8"	: (1, "B"),
          "int16"	: (2, "h"),
          "uint16"	: (2, "H"),
          "int32"	: (4, "i"),
          "uint32"	: (4, "I"),
          "char"	: (1, "s"),
         }

_struct = dict()

class Descriptor :
    def __init__(self, tag) :
        self.tag = tag

    def __get__(self, obj, owner = None) :
        if self.tag not in obj._tag :
            raise AttributeError("Struct {} has no member  {}.".format(obj._name, self.tag))
        (typ, sig, pos) = obj._tag[self.tag]

        if typ in _struct :
            (siz, sig) = _type[typ]
            val = Struct(typ, memoryview(obj._data)[pos:pos+siz])
        else :
            val = struct.unpack_from(sig, obj._data, pos)
            if len(val) == 1 : val = val[0]
            
        return val
        
    def __set__(self, obj, val) :
        if self.tag not in obj._tag :
            raise AttributeError("Struct {} has no member  {}.".format(obj._name, self.tag))
        (typ, sig, pos) = obj._tag[self.tag]
        
        if typ in _struct : val = val._data
        if not (isinstance(val, list) or isinstance(val, tuple)) : val = [ val ]
        struct.pack_into(sig, obj._data, pos, *val)

        
class Struct :
    __slots__ = [ "_name", "_tag", "_data" ]	# has no effect on uPython
    
    @classmethod
    def define(cls, name, format, padding = None) :
        pos = 0
        tag = dict()
        for x in format.split(";") :
            x = x.split()
            if len(x) == 0 : break;	# last item
            (typ, nam) = x
            if nam in cls.__slots__ :
                raise ValueError("Reserved variable name: {}".format(nam))
            setattr(cls, nam, Descriptor(nam))
            
            n = typ.find("[")
            if n < 0 :
                n = ""
            else :
                (typ, n) = (typ[:n], typ[n+1:-1])
                if typ in _struct : raise ValueError("Array of structure is not supported.")

            (siz, sig) = _type[typ]

            if padding and sig[-1] != "s" and siz > 1 :
                if pos & 0x01 : pos += 1
                if siz == 4 and padding >= 4 and pos & 0x02 : pos += 2
            
            tag[nam] = (typ, "<" + n + sig, pos)
            if n != "" : siz *= int(n)
            pos += siz

        _type[name]   = (pos, str(pos) + "s")
        _struct[name] = tag

    @staticmethod
    def get_info(name = None) :
        if name is None : return list(_struct.keys())
        return _type[name], _struct[name]
            
    def __init__(self, name, data = None) :
        if name not in _struct : raise ValueError("Struct {} is not defined.".format(name))
        self._name = name
        self._tag = _struct[name]
        
        (siz, sig) = _type[name]
        if data is None :
            data = bytearray(siz)
        else :
            if len(data) != siz : raise ValueError("Size of data does not match to struct {}.".format(name))
        self._data = data

