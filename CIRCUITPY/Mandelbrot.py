import time
import array
import board
import displayio as dpio
from ButtonEvents import ButtonEvents
from micropython import const

WIDTH    = const(160)	# Half width
HEIGHT   = const(120)	# Half height
MAX_LOOP = const(128)

bmp = dpio.Bitmap(WIDTH * 2, HEIGHT * 2, 256)
pal = dpio.Palette(256)

for i in range(256) :
    k = (i & 0x7) << 5
    j = (i >> 3) % 6
    if   j == 0 : pal[i] = k
    elif j == 1 : pal[i] = (k <<  8) + 0x0000FF
    elif j == 2 : pal[i] = (k << 16) + 0x00FFFF
    elif j == 3 : pal[i] = (0xFF - k) + 0xFFFF00
    elif j == 4 : pal[i] = ((0xFF - k) <<  8) + 0xFF0000
    else        : pal[i] = ((0xFF - k) << 16)
pal[MAX_LOOP] = 0x000000    # Mandelbrot set

buf = memoryview(bmp)

disp = board.DISPLAY
tg = dpio.TileGrid(bmp, pixel_shader = pal)
g  = dpio.Group()
g.append(tg)
disp.show(g)

# r0 : bytearray(WIDTH x HEIGHT)
# r1 : array.array("f", (0.0, 2.0, 4.0, center-x, center-y, step))
@micropython.asm_thumb
def mandel(r0, r1):
    vldr(s10, [r1, 0])	# 0.0
    vldr(s11, [r1, 4])	# 2.0
    vldr(s12, [r1, 8])	# 4.0
    vldr(s13, [r1, 12])	# cx
    vldr(s14, [r1, 16])	# cy
    vldr(s15, [r1, 20])	# step

    mov(r4, HEIGHT)	# y
    neg(r4, r4)
    label(loop_y)
    vmov(s4, r4)
    vcvt_f32_s32(s4, s4)
    vmul(s4, s4, s15)	# cb = y * step + cy
    vadd(s4, s4, s14)
    mov(r3, WIDTH)	# x
    neg(r3, r3)
    label(loop_x)
    vmov(s3, r3)
    vcvt_f32_s32(s3, s3)
    vmul(s3, s3, s15)	# ca = x * step + cx
    vadd(s3, s3, s13)
    vadd(s0, s3, s10)	# a = ca
    vadd(s1, s4, s10)	# b = cb
    vmul(s20, s0, s0)	# a*a
    vmul(s21, s1, s1) 	# b*b
    mov(r5, 0)
    label(loop_i)
    vmul(s1, s0, s1)	# b *= a
    vmul(s1, s1, s11)	# b *= 2.0
    vadd(s1, s1, s4)	# b += cb
    vsub(s0, s20, s21)	# a = a*a - b*b
    vadd(s0, s0, s3)	# a += ca
    vmul(s20, s0, s0)	# a*a
    vmul(s21, s1, s1)	# b*b
    vadd(s22, s20, s21)	# a*a + b*b
    vcmp(s22, s12)	# a*a + b*b vs 4.0
    vmrs(APSR_nzcv, FPSCR)
    bgt(loop_i_exit)
    add(r5, 1)
    cmp(r5, MAX_LOOP)
    blt(loop_i)
    label(loop_i_exit)
    strb(r5, [r0, 0])
    add(r0, 1)
    add(r3, 1)
    cmp(r3, WIDTH)
    blt(loop_x)
    add(r4, 1)
    cmp(r4, HEIGHT)
    blt(loop_y)

param = array.array("f", (0.0, 2.0, 4.0, -0.7, 0.0, 0.0125 ))
mandel(buf, param)
bmp.dirty()

be = ButtonEvents()
while True :
    b = be.keys()
    if b == 0 :
        time.sleep(0.05)
        continue
    elif b & be.K_SELECT :
        break
    elif b & be.K_X :
        print(param[3], param[4], param[5])
        continue
    elif b & be.K_LEFT :
        cx = param[3] - 16 * param[5]
        if cx < -2.3 : continue
        param[3] = cx
    elif b & be.K_RIGHT :
        cx = param[3] + 16 * param[5]
        if cx > 0.9 : continue
        param[3] = cx
    elif b & be.K_UP :
        cy = param[4] - 16 * param[5]
        if cy < -1.2 : continue
        param[4] = cy
    elif b & be.K_DOWN :
        cy = param[4] + 16 * param[5]
        if cy > 1.2 : continue
        param[4] = cy
    elif b & be.K_O :
        step = param[5] / 2.0
        if step < 0.5e-7 : continue
        param[5] = step
    elif b & be.K_START :
        step = param[5] * 2.0
        if step > 0.0125 : continue
        param[5] = step
            
    t0 = time.monotonic_ns()
    mandel(buf, param)
    t1 = time.monotonic_ns()
    print(f"{(t1 - t0)*1e-6} msec")

    bmp.dirty()

