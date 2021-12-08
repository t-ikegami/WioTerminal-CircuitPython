import uctypes as ct

GCLK_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SYNCBUSY'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GENCTRL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS | 12 << ct.BF_LEN,
  }),
  'GENCTRL'	: ( 0x20 | ct.ARRAY, 12, {
    'reg'	:   0x00 | ct.UINT32,
    'SRC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'GENEN'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'IDC'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'OOV'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'OE'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DIVSEL'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'DIV'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'PCHCTRL'	: ( 0x80 | ct.ARRAY, 48, {
    'reg'	:   0x00 | ct.UINT32,
    'GEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'CHEN'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'WRTLOCK'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

GCLK = ct.struct(0x40001c00, GCLK_, ct.LITTLE_ENDIAN)
