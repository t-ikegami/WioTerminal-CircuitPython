import uctypes as ct

OSCCTRL_DPLL = {
  'DPLLCTRLA'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DPLLRATIO'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'LDR'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 13 << ct.BF_LEN,
    'LDRFRAC'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  5 << ct.BF_LEN,
  }),
  'DPLLCTRLB'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'FILTER'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  4 << ct.BF_LEN,
    'WUF'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'REFCLK'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  3 << ct.BF_LEN,
    'LTIME'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  3 << ct.BF_LEN,
    'LBYPASS'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DCOFILTER'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  3 << ct.BF_LEN,
    'DCOEN'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'DIV'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS | 11 << ct.BF_LEN,
  }),
  'DPLLSYNCBUSY'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLLRATIO'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DPLLSTATUS'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'LOCK'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'CLKRDY'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
}

OSCCTRL_ = {
  'EVCTRL'	: ( 0x00, {
    'reg'	:   0x00 | ct.UINT8,
    'CFDEO0'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'CFDEO1'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENCLR'	: ( 0x04, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSCRDY0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCRDY1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL0'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL1'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLOOB'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKF'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRCS'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKR'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKF'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LTO'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LDRTO'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKR'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKF'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LTO'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LDRTO'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTENSET'	: ( 0x08, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSCRDY0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCRDY1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL0'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL1'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLOOB'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKF'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRCS'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKR'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKF'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LTO'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LDRTO'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKR'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKF'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LTO'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LDRTO'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'INTFLAG'	: ( 0x0C, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSCRDY0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCRDY1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL0'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL1'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLOOB'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKF'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRCS'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKR'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKF'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LTO'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LDRTO'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKR'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKF'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LTO'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LDRTO'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'STATUS'	: ( 0x10, {
    'reg'	:   0x00 | ct.UINT32,
    'XOSCRDY0'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCRDY1'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL0'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCFAIL1'	:   0x00 | ct.BFUINT32 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCCKSW0'	:   0x00 | ct.BFUINT32 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'XOSCCKSW1'	:   0x00 | ct.BFUINT32 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRDY'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLOOB'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKF'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLLCKC'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLRCS'	:   0x00 | ct.BFUINT32 | 12 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKR'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LCKF'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0TO'	:   0x00 | ct.BFUINT32 | 18 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL0LDRTO'	:   0x00 | ct.BFUINT32 | 19 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKR'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LCKF'	:   0x00 | ct.BFUINT32 | 25 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1TO'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  1 << ct.BF_LEN,
    'DPLL1LDRTO'	:   0x00 | ct.BFUINT32 | 27 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'XOSCCTRL'	: ( 0x14 | ct.ARRAY, 2, {
    'reg'	:   0x00 | ct.UINT32,
    'ENABLE'	:   0x00 | ct.BFUINT32 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'XTALEN'	:   0x00 | ct.BFUINT32 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT32 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT32 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
    'LOWBUFGAIN'	:   0x00 | ct.BFUINT32 |  8 << ct.BF_POS |  1 << ct.BF_LEN,
    'IPTAT'	:   0x00 | ct.BFUINT32 |  9 << ct.BF_POS |  2 << ct.BF_LEN,
    'IMULT'	:   0x00 | ct.BFUINT32 | 11 << ct.BF_POS |  4 << ct.BF_LEN,
    'ENALC'	:   0x00 | ct.BFUINT32 | 15 << ct.BF_POS |  1 << ct.BF_LEN,
    'CFDEN'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  1 << ct.BF_LEN,
    'SWBEN'	:   0x00 | ct.BFUINT32 | 17 << ct.BF_POS |  1 << ct.BF_LEN,
    'STARTUP'	:   0x00 | ct.BFUINT32 | 20 << ct.BF_POS |  4 << ct.BF_LEN,
    'CFDPRESC'	:   0x00 | ct.BFUINT32 | 24 << ct.BF_POS |  4 << ct.BF_LEN,
  }),
  'DFLLCTRLA'	: ( 0x1C, {
    'reg'	:   0x00 | ct.UINT8,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'RUNSTDBY'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'ONDEMAND'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DFLLCTRLB'	: ( 0x20, {
    'reg'	:   0x00 | ct.UINT8,
    'MODE'	:   0x00 | ct.BFUINT8 |  0 << ct.BF_POS |  1 << ct.BF_LEN,
    'STABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'LLAW'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'USBCRM'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'CCDIS'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
    'QLDIS'	:   0x00 | ct.BFUINT8 |  5 << ct.BF_POS |  1 << ct.BF_LEN,
    'BPLCKC'	:   0x00 | ct.BFUINT8 |  6 << ct.BF_POS |  1 << ct.BF_LEN,
    'WAITLOCK'	:   0x00 | ct.BFUINT8 |  7 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DFLLVAL'	: ( 0x24, {
    'reg'	:   0x00 | ct.UINT32,
    'FINE'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS |  8 << ct.BF_LEN,
    'COARSE'	:   0x00 | ct.BFUINT32 | 10 << ct.BF_POS |  6 << ct.BF_LEN,
    'DIFF'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS | 16 << ct.BF_LEN,
  }),
  'DFLLMUL'	: ( 0x28, {
    'reg'	:   0x00 | ct.UINT32,
    'MUL'	:   0x00 | ct.BFUINT32 |  0 << ct.BF_POS | 16 << ct.BF_LEN,
    'FSTEP'	:   0x00 | ct.BFUINT32 | 16 << ct.BF_POS |  8 << ct.BF_LEN,
    'CSTEP'	:   0x00 | ct.BFUINT32 | 26 << ct.BF_POS |  6 << ct.BF_LEN,
  }),
  'DFLLSYNC'	: ( 0x2C, {
    'reg'	:   0x00 | ct.UINT8,
    'ENABLE'	:   0x00 | ct.BFUINT8 |  1 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLCTRLB'	:   0x00 | ct.BFUINT8 |  2 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLVAL'	:   0x00 | ct.BFUINT8 |  3 << ct.BF_POS |  1 << ct.BF_LEN,
    'DFLLMUL'	:   0x00 | ct.BFUINT8 |  4 << ct.BF_POS |  1 << ct.BF_LEN,
  }),
  'DPLL'	: ( 0x30 | ct.ARRAY, 2, OSCCTRL_DPLL ),
}

OSCCTRL = ct.struct(0x40001000, OSCCTRL_)
