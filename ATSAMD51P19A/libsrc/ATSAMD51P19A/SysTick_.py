import uctypes as ct

SysTick_ = {
  'CSR'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'TICKINT'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLKSOURCE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'COUNTFLAG'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'RVR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'RELOAD'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'CVR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'CURRENT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
  }),
  'CALIB'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'TENMS'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 24 << ct.BF_LEN,
    'SKEW'	:   0x00 | ct.BFUINT32 | 30 << ct.BF_POS |  1 << ct.BF_LEN,
    'NOREF'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

SysTick = ct.struct(0xe000e010, SysTick_)
