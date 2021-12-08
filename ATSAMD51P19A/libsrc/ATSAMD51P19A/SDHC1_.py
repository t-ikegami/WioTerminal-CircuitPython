import uctypes as ct
from .SDHC0_ import SDHC_

SDHC1 = ct.struct(0x46000000, SDHC_, ct.LITTLE_ENDIAN)
