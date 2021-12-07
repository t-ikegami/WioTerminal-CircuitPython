import uctypes as ct

FPU_ = {
  'FPCCR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'LSPACT'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'USER'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'THREAD'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'HFRDY'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'MMRDY'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'BFRDY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'MONRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'LSPEN'	:   0x00 | ct.BFUINT32 | 30 << ct.BF_POS |  1 << ct.BF_LEN,
    'ASPEN'	:   0x00 | ct.BFUINT32 | 31 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'FPCAR'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'ADDRESS'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS | 29 << ct.BF_LEN,
  }),
  'FPDSCR'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'RMODE'	:   0x00 | ct.BFUINT32 | 22 << ct.BF_POS |  2 << ct.BF_LEN,
    'FZ'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DN'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'AHP'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'MVFR0'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'A_SIMD_registers'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'Single_precision'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
    'Double_precision'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  4 << ct.BF_LEN,
    'FP_excep_trapping'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  4 << ct.BF_LEN,
    'Divide'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  4 << ct.BF_LEN,
    'Square_root'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  4 << ct.BF_LEN,
    'Short_vectors'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
    'FP_rounding_modes'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'MVFR1'	: ( 0x14, {
    'reg'	:   0x00 | ct.UINT32,
    'FtZ_mode'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'D_NaN_mode'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  4 << ct.BF_LEN,
    'FP_HPFP'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
    'FP_fused_MAC'	:   0x00 | ct.BFUINT32 | 28 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
}

FPU = ct.struct(0xe000ef30, FPU_)
