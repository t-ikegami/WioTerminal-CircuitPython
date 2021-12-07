import uctypes as ct

HMATRIXB_PRS = {
  'PRAS'	: 0x00 | ct.UINT32,
  'PRBS'	: 0x04 | ct.UINT32,
}

HMATRIXB_ = {
  'PRS'	: ( 0x80 | ct.ARRAY, 16, HMATRIXB_PRS ),
}

HMATRIX = ct.struct(0x4100c000, HMATRIXB_)
