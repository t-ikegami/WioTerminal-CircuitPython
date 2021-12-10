# Parse SVD file to generate MCU register accessors by micropython
# uctypes.  To reduce memory usage, only requied peripherals are
# imported on-demand by preparing __getattr__ function on the device
# module generated.  Tested only on ATSAMD51P19A.svd:
#
#   python3 svd2ctypes.py ATSAMD51P19A.svd
#
# A module directory ATSAMD51P19A is created.
#
from collections import namedtuple
import xml.etree.ElementTree as ET

bitfield = namedtuple("bitfield", "name offset width")

# In the original uctypes, sizeof(struct) is calculated with padding
# included.  However, the calculated size is dependent on the order of
# keys in dict that defines the structure.  The padding is removed if
# we specify LITTLE_ENDIAN layout explicitly, though write to
# registers becomes not atomic.  Different from ctypes in CPython, the
# memory layout of struct is specified explicitly including padding.
# Therefore, I have disabled the padding calculation of uctypes in the
# custom firmware, and employed the NATIVE layout.

# LAYOUT = ", ct.LITTLE_ENDIAN"			# NATIVE add fillers to calculate sizeof struct; this is fixed.
LAYOUT = ""

def get_text(xml, tag, default = False) :
    node = xml.find(tag)
    if node is None :
        if default is False : raise ValueError(f"No tag {tag} found.")
        return default
    return node.text

def get_int(xml, tag, default = False) :
    node = xml.find(tag)
    if node is None :
        if default is False : raise ValueError(f"No tag {tag} found.")
        return default
    return int(node.text, 0)

class Device :
    def __init__(self, svd_file) :
        self.xml = xml = ET.parse(svd_file).getroot()
        self.name = get_text(xml, "name")
        self.peripherals = []
        p_dict = {}
        for x in xml.findall("./peripherals/peripheral") :
            p = Peripheral(x)
            if p.name in p_dict : raise ValueError("Collision of peripheral names: " + p.name)
            self.peripherals.append(p)
            p_dict[p.name] = p
            if p.parent is not None : p.parent = p_dict[p.parent]

    def dump(self) :
        import os
        os.mkdir(self.name)
        os.chdir(self.name)
        with open("__init__.py", "w") as f :
            f.write("""\
def __getattr__(key) :
    mod = __import__(key + "_", globals(), None, [], 1)
    return getattr(mod, key)
""")
        for p in self.peripherals :
            with open(f"{p.name}_.py", "w") as f :
                f.write(p.dump())
                
class Peripheral :
    def __init__(self, xml) :
        self.xml  = xml
        self.name = get_text(xml, "name")
        self.base = get_int(xml, "baseAddress")
        self.prefix = get_text(xml, "prependToName", None)
        self.parent = None

        parent = xml.get("derivedFrom")
        if parent is not None :
            if xml.find("registers") :
                raise ValueError("Registers of a derived peripheral should be identical to its parent.")
            self.parent = parent
            return

        regs = xml.findall("registers")
        assert len(regs) == 1
        regs = regs[0]
        self.regs = []
        for r in regs :
            if r.tag == "register" :
                self.regs.append(Register(r))
            elif r.tag == "cluster" :
                self.regs.append(Cluster(r))
            else :
                raise ValueError("Unexpected tag in registers: " + r.tag)

    def dump(self) :
        defs = [ "import uctypes as ct" ]
        if self.parent is not None :
            defs.append( f"from .{self.parent.name}_ import {self.parent.prefix}\n" )
            defs.append( f"{self.name} = ct.struct({hex(self.base)}, {self.parent.prefix}{LAYOUT})\n" )
        else :
            defs.append("")
            for r in self.regs :
                if isinstance(r, Cluster) :
                    defs.append( r.dump_def(self.prefix) )

            defs.append( f"{self.prefix} = " "{" )
            for r in self.regs :
                defs.append(r.dump())
            defs.append("}\n")

            defs.append( f"{self.name} = ct.struct({hex(self.base)}, {self.prefix}{LAYOUT})\n" )
        
        return "\n".join(defs)
        
class Register :
    def __init__(self, xml) :
        if isinstance(xml, int) :	# filler used to fix the size of cluster to xml
            self.name = "DUMMY_FILLER"
            self.offset = xml - 1
            self.size   = 8
            self.dim    = 1
            self.fields = None
            return
        
        self.name   = get_text(xml, "name")
        self.offset = get_int(xml, "addressOffset")
        self.size   = get_int(xml, "size")
        self.dim    = get_int(xml, "dim", None)
        if self.dim is None :
            self.dim = 1
        else :
            # [%s] is inserted even if dim == 1
            self.name = self.name[:self.name.index("[")]	# raise if not found
            dimIncrement = get_int(xml, "dimIncrement")
            assert dimIncrement * 8 == self.size
            
        self.fields = None
        
        fields = xml.find("fields")
        if fields is None : return

        def parse_fields(xml) :
            assert xml.tag == "field"
            name   = get_text(xml, "name")
            offset = get_int(xml, "bitOffset")
            width  = get_int(xml, "bitWidth")

            # remove trailing "_"
            name = name.removesuffix("_")
            return bitfield(name, offset, width)
            
        fields = [ parse_fields(x) for x in fields ]
        if len(fields) == 1 and fields[0].width == self.size : return
        self.fields = fields

    def dump(self) :
        name = self.name
        offset = f"0x{self.offset:02X}"
        ctype = { 8 : "UINT8", 16 : "UINT16", 32 : "UINT32" }[self.size]
        dim = self.dim

        if self.fields is None :
            if dim == 1 :
                return f"  '{name}'\t: {offset} | ct.{ctype},"
            else :
                return f"  '{name}'\t: ( {offset} | ct.ARRAY, {dim} | ct.{ctype} ),"
            
        if dim == 1 :
            union = [ f"  '{name}'\t: ( {offset}, " "{", ]
        else :
            union = [ f"  '{name}'\t: ( {offset} | ct.ARRAY, {dim}, " "{", ]

        union.append( f"    'reg'\t:   0x00 | ct.{ctype}," )
        for f in self.fields :
            union.append( f"    '{f.name}'\t:   0x00 | ct.BF{ctype} |"
                          f" {f.offset:2d} << ct.BF_POS | {f.width:2d} << ct.BF_LEN," )
        union.append( "  })," )

        return "\n".join(union)
            
class Cluster :
    def __init__(self, xml) :
        self.name   = get_text(xml, "name")
        self.offset = get_int(xml, "addressOffset")
        self.dim = get_int(xml, "dim", None)
        if self.dim is None :
            self.dim = 1
            dimIncrement = None
        else :
            self.name = self.name[:self.name.index("[")]	# raise if not found
            dimIncrement = get_int(xml, "dimIncrement")
            
        self.regs = []
        for x in xml :
            if x.tag == "register" :
                self.regs.append(Register(x))
            elif x.tag == "cluster" :
                self.regs.append(Cluster(x))
            else :
                # Ignore other tags
                pass

        # calculate size
        size = max( r.size * r.dim / 8 + r.offset for r in self.regs)
        assert size == int(size)
        size = int(size)		# size in bytes
        self.size = int(size) * 8	# size in bits
        
        if dimIncrement is not None :
            assert size <= dimIncrement
            if size < dimIncrement :                # add dummy filler
                self.regs.append(Register(dimIncrement))
                self.size = dimIncrement * 8
                print(f"Insert filler to cluster {self.name}: {hex(size)} → {hex(dimIncrement)}.")
            # size = max( int(r.size) * int(r.dim) / 8 + int(r.offset, 0) for r in self.regs)
            # print( self.name, size, int(self.size) / 8, dimIncrement )

    def dump_def(self, prefix) :
        self.dump_name = f"{prefix}{self.name}"

        defs = []
        for r in self.regs :
            if isinstance(r, Cluster) :
                defs.append(r.dump_def( f"{self.dump_name}_" ))
        
        defs.append( f"{self.dump_name} = " "{" )
        for r in self.regs : defs.append(r.dump())
        defs.append("}\n")
        return "\n".join(defs)
            
    def dump(self) :
        name = self.name
        offset = f"0x{self.offset:02X}"
        ctype = self.dump_name
        dim = self.dim

        if dim == 1 :
            return f"  '{name}'\t: ( {offset}, {ctype} ),"
        else :
            return f"  '{name}'\t: ( {offset} | ct.ARRAY, {dim}, {ctype} ),"
            
if __name__ == "__main__" :
    import sys

    dev = Device(sys.argv[1])
    dev.dump()

    # dev = Device("ATSAMD51P19A.svd")
    # print(dev.name)
    # print([ x.name for x in dev.peripherals ])
    # print(dev.peripherals[24].dump())
