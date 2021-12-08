import uctypes as ct

NVIC_ = {
  'ISER'	: ( 0x00 | ct.ARRAY, 5 | ct.UINT32 ),
  'ICER'	: ( 0x80 | ct.ARRAY, 5 | ct.UINT32 ),
  'ISPR'	: ( 0x100 | ct.ARRAY, 5 | ct.UINT32 ),
  'ICPR'	: ( 0x180 | ct.ARRAY, 5 | ct.UINT32 ),
  'IABR'	: ( 0x200 | ct.ARRAY, 5 | ct.UINT32 ),
  'IP'	: ( 0x300 | ct.ARRAY, 35, {
    'reg'	:   0x00 | ct.UINT8,
    'PRI0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
  }),
  'STIR'	: ( 0xE00, {
    'reg'	:   0x00 | ct.UINT32,
    'INTID'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  9 << ct.BF_LEN,
  }),
}

NVIC = ct.struct(0xe000e100, NVIC_, ct.LITTLE_ENDIAN)
