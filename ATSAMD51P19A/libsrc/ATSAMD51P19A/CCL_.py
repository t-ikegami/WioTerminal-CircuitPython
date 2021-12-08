import uctypes as ct

CCL_ = {
  'CTRL'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SEQCTRL'	: ( 0x04 | ct.ARRAY, 2, {
    'reg'	:   0x00 | ct.UINT8,
    'SEQSEL'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'LUTCTRL'	: ( 0x08 | ct.ARRAY, 4, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'FILTSEL'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'EDGESEL'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'INSEL0'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'INSEL1'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  4 << ct.BF_LEN,
    'INSEL2'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  4 << ct.BF_LEN,
    'INVEI'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUTEI'	:   0x00 | ct.BFUINT32 | 21 << ct.BF_POS |  1 << ct.BF_LEN,
    'LUTEO'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRUTH'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
}

CCL = ct.struct(0x42003800, CCL_, ct.LITTLE_ENDIAN)
