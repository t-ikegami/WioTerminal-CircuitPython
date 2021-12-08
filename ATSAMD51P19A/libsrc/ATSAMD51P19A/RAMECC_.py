import uctypes as ct

RAMECC_ = {
  'INTENCLR'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SINGLEE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DUALE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'SINGLEE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DUALE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT8,
    'SINGLEE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DUALE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x03, {
    'reg'	:   0x00 | ct.UINT8,
    'ECCDIS'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'ERRADDR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'ERRADDR'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 17 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x0F, {
    'reg'	:   0x00 | ct.UINT8,
    'ECCDIS'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ECCELOG'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

RAMECC = ct.struct(0x41020000, RAMECC_, ct.LITTLE_ENDIAN)
