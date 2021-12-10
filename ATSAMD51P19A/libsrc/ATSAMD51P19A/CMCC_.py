import uctypes as ct

CMCC_ = {
  'TYPE'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'GCLK'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RRP'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'WAYNUM'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  2 << ct.BF_LEN,
    'LCKDOWN'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'CSIZE'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'CLSIZE'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'CFG'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'ICDIS'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DCDIS'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'CSIZESW'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'CTRL'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'CEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'SR'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'CSTS'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'LCKWAY'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'LCKWAY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'MAINT0'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT32,
    'INVALL'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'MAINT1'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT32,
    'INDEX'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  8 << ct.BF_LEN,
    'WAY'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'MCFG'	: ( 0x28, {
    'reg'	:   0x00 | ct.UINT32,
    'MODE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'MEN'	: ( 0x2C, {
    'reg'	:   0x00 | ct.UINT32,
    'MENABLE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'MCTRL'	: ( 0x30, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'MSR'	: 0x34 | ct.UINT32,
}

CMCC = ct.struct(0x41006000, CMCC_)
