import uctypes as ct

DSU_ = {
  'CTRL'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'SWRST'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'CRC'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'MBIST'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CE'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'ARR'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'SMSA'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSA'	: ( 0x01, {
    'reg'	:   0x00 | ct.UINT8,
    'DONE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'CRSTEXT'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'BERR'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'FAIL'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'PERR'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUSB'	: ( 0x02, {
    'reg'	:   0x00 | ct.UINT8,
    'PROT'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'DBGPRES'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DCCD0'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'DCCD1'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'HPE'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'CELCK'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'TDCCD0'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'TDCCD1'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'ADDR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'AMOD'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'ADDR'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS | 30 << ct.BF_LEN,
  }),
  'LENGTH'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'LENGTH'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS | 30 << ct.BF_LEN,
  }),
  'DATA'	: 0x0C | ct.UINT32,
  'DCC'	: ( 0x10 | ct.ARRAY, 2 | ct.UINT32 ),
  'DID'	: ( 0x18, {
    'reg'	:   0x00 | ct.UINT32,
    'DEVSEL'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
    'REVISION'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'DIE'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  4 << ct.BF_LEN,
    'SERIES'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  6 << ct.BF_LEN,
    'FAMILY'	:   0x00 | ct.BFUINT32 | 23 << ct.BF_POS |  5 << ct.BF_LEN,
    'PROCESSOR'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'CFG'	: ( 0x1C, {
    'reg'	:   0x00 | ct.UINT32,
    'LQOS'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  2 << ct.BF_LEN,
    'DCCDMALEVEL'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  2 << ct.BF_LEN,
    'ETBRAMEN'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DCFG'	: ( 0xF0 | ct.ARRAY, 2 | ct.UINT32 ),
  'ENTRY0'	: ( 0x1000, {
    'reg'	:   0x00 | ct.UINT32,
    'EPRES'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'FMT'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'ADDOFF'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS | 20 << ct.BF_LEN,
  }),
  'ENTRY1'	: 0x1004 | ct.UINT32,
  'END'	: 0x1008 | ct.UINT32,
  'MEMTYPE'	: ( 0x1FCC, {
    'reg'	:   0x00 | ct.UINT32,
    'SMEMP'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'PID4'	: ( 0x1FD0, {
    'reg'	:   0x00 | ct.UINT32,
    'JEPCC'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'FKBC'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'PID5'	: 0x1FD4 | ct.UINT32,
  'PID6'	: 0x1FD8 | ct.UINT32,
  'PID7'	: 0x1FDC | ct.UINT32,
  'PID0'	: ( 0x1FE0, {
    'reg'	:   0x00 | ct.UINT32,
    'PARTNBL'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'PID1'	: ( 0x1FE4, {
    'reg'	:   0x00 | ct.UINT32,
    'PARTNBH'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'JEPIDCL'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'PID2'	: ( 0x1FE8, {
    'reg'	:   0x00 | ct.UINT32,
    'JEPIDCH'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  3 << ct.BF_LEN,
    'JEPU'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'REVISION'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'PID3'	: ( 0x1FEC, {
    'reg'	:   0x00 | ct.UINT32,
    'CUSMOD'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'REVAND'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'CID0'	: ( 0x1FF0, {
    'reg'	:   0x00 | ct.UINT32,
    'PREAMBLEB0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'CID1'	: ( 0x1FF4, {
    'reg'	:   0x00 | ct.UINT32,
    'PREAMBLE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'CCLASS'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'CID2'	: ( 0x1FF8, {
    'reg'	:   0x00 | ct.UINT32,
    'PREAMBLEB2'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
  'CID3'	: ( 0x1FFC, {
    'reg'	:   0x00 | ct.UINT32,
    'PREAMBLEB3'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
  }),
}

DSU = ct.struct(0x41002000, DSU_)
