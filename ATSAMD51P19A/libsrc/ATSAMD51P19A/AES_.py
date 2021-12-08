import uctypes as ct

AES_ = {
  'CTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT32,
    'SWRST'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'AESMODE'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  3 << ct.BF_LEN,
    'CFBS'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
    'KEYSIZE'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  2 << ct.BF_LEN,
    'CIPHER'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'STARTMODE'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'LOD'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'KEYGEN'	:   0x00 | ct.BFUINT32 | 13 << ct.BF_POS |  1 << ct.BF_LEN,
    'XORKEY'	:   0x00 | ct.BFUINT32 | 14 << ct.BF_POS |  1 << ct.BF_LEN,
    'CTYPE'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'CTRLB'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT8,
    'START'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'NEWMSG'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'EOM'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'GFMUL'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x05, {
    'reg'	:   0x00 | ct.UINT8,
    'ENCCMP'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GFMCMP'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x06, {
    'reg'	:   0x00 | ct.UINT8,
    'ENCCMP'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GFMCMP'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x07, {
    'reg'	:   0x00 | ct.UINT8,
    'ENCCMP'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'GFMCMP'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DATABUFPTR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT8,
    'INDATAPTR'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
  }),
  'DBGCTRL'	: ( 0x09, {
    'reg'	:   0x00 | ct.UINT8,
    'DBGRUN'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'KEYWORD'	: ( 0x0C | ct.ARRAY, 8 | ct.UINT32 ),
  'INDATA'	: 0x38 | ct.UINT32,
  'INTVECTV'	: ( 0x3C | ct.ARRAY, 4 | ct.UINT32 ),
  'HASHKEY'	: ( 0x5C | ct.ARRAY, 4 | ct.UINT32 ),
  'GHASH'	: ( 0x6C | ct.ARRAY, 4 | ct.UINT32 ),
  'CIPLEN'	: 0x80 | ct.UINT32,
  'RANDSEED'	: 0x84 | ct.UINT32,
}

AES = ct.struct(0x42002400, AES_, ct.LITTLE_ENDIAN)
