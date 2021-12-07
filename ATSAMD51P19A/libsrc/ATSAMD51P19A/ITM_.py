import uctypes as ct

ITM_ = {
  'PORT_WORD_MODE'	: ( 0x00 | ct.ARRAY, 32 | ct.UINT32 ),
  'PORT_BYTE_MODE'	: ( 0x00 | ct.ARRAY, 32, {
    'reg'	:   0x00 | ct.UINT32,
    'PORT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'PORT_HWORD_MODE'	: ( 0x00 | ct.ARRAY, 32, {
    'reg'	:   0x00 | ct.UINT32,
    'PORT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'TER'	: 0xE00 | ct.UINT32,
  'TPR'	: ( 0xE40, {
    'reg'	:   0x00 | ct.UINT32,
    'PRIVMASK'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'TCR'	: ( 0xE80, {
    'reg'	:   0x00 | ct.UINT32,
    'ITMENA'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TSENA'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'SYNCENA'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'DWTENA'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWOENA'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'STALLENA'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TSPrescale'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'GTSFREQ'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  2 << ct.BF_LEN,
    'TraceBusID'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  7 << ct.BF_LEN,
    'BUSY'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'IWR'	: ( 0xEF8, {
    'reg'	:   0x00 | ct.UINT32,
    'ATVALIDM'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'IRR'	: ( 0xEFC, {
    'reg'	:   0x00 | ct.UINT32,
    'ATREADYM'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

ITM = ct.struct(0xe0000000, ITM_)
