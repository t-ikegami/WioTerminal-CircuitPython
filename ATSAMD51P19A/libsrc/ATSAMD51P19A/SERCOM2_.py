import uctypes as ct
from .SERCOM0_ import SERCOM_

SERCOM2 = ct.struct(0x41012000, SERCOM_, ct.LITTLE_ENDIAN)
