import uctypes as ct

CoreDebug_ = {
  'DHCSR'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'C_DEBUGEN'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'C_HALT'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'C_STEP'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'C_MASKINTS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'C_SNAPSTALL'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'S_REGRDY'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'S_HALT'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'S_SLEEP'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'S_LOCKUP'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'S_RETIRE_ST'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'S_RESET_ST'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DBGKEY'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'DCRSR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'REGSEL'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  5 << ct.BF_LEN,
    'REGWnR'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DCRDR'	: 0x08 | ct.UINT32,
  'DEMCR'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'VC_CORERESET'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_MMERR'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_NOCPERR'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_CHKERR'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_STATERR'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_BUSERR'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_INTERR'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'VC_HARDERR'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'MON_EN'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'MON_PEND'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'MON_STEP'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'MON_REQ'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'TRCENA'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

CoreDebug = ct.struct(0xe000edf0, CoreDebug_, ct.LITTLE_ENDIAN)
