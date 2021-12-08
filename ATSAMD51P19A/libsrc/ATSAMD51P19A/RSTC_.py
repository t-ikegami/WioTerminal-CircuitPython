import uctypes as ct

RSTC_ = {
  'RCAUSE'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'POR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'BODCORE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'BODVDD'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'NVM'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'EXT'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'WDT'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'SYST'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'BACKUP'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'BKUPEXIT'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT8,
    'RTC'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'BBPS'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'HIB'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

RSTC = ct.struct(0x40000c00, RSTC_, ct.LITTLE_ENDIAN)
