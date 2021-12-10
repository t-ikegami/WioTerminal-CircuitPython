import uctypes as ct

PCC_ = {
  'MR'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'PCEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DSIZE'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  2 << ct.BF_LEN,
    'SCALE'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'ALWYS'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'HALFS'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'FRSTS'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'ISIZE'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  3 << ct.BF_LEN,
    'CID'	:   0x00 | ct.BFUINT32 | 30 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'IER'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'DRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVRE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'IDR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'DRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVRE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'IMR'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'DRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVRE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'ISR'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'DRDY'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'OVRE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'RHR'	: 0x14 | ct.UINT32,
  'WPMR'	: ( 0xE0, {
    'reg'	:   0x00 | ct.UINT32,
    'WPEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'WPKEY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'WPSR'	: ( 0xE4, {
    'reg'	:   0x00 | ct.UINT32,
    'WPVS'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'WPVSRC'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
}

PCC = ct.struct(0x43002c00, PCC_)
