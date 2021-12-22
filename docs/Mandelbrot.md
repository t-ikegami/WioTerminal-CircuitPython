# マンデルブロベンチマーク

## 概要
こちらの~~パクリ~~移植。<br/>
http://radiopench.blog96.fc2.com/blog-entry-1150.html <br/>

| オリジナル (C 言語) | 31.15 ms |
| 単純移植版          |   445 ms |
| 高速版              |  3.17 ms |

## 単純移植版
C 言語で書かれたオリジナルをほぼそのまま Python 化しました。

```
import gc
import time
result = bytearray(25 * 79)

def mandel() :
    calcCount = 0
    idx = 0
    for y in range(-12, 13) :
        for x in range(-39, 40) :
            ca = float(x) * 0.0458
            cb = float(y) * 0.08333
            a  = ca
            b  = cb
            for i in range(16) :
 	        calcCount += 1
                t = a * a - b * b + ca
                b = 2.0 * a * b + cb
                a = t
                if (a * a + b * b) > 4.0 :
 	            result[idx] = i
                    break
 	        else :
 	            result[idx] = 16
            idx += 1
    return calcCount

gc.collect()
gc.disable()
t0 = time.monotonic_ns()
calcCount = mandel()
t1 = time.monotonic_ns()
gc.enable()
print(f"\n{(t1 - t0)*1e-3} us, calc count = {calcCount}")

tbl = "0123456789ABCDEF "
idx = 0
for y in range(-12, 13) :
    for x in range(-39, 40) :
        print(tbl[result[idx]], end = "")
        idx += 1
    print()
```

445 ms でした。C 版に比べると 15 倍くらい遅くなります。


## 高速版
実行にはこちらの [ファームウェア](/Firmware/MyCircuitPython7.0+NATIVE-STAGE.uf2) が必要になります。

```
import gc
import time
import array
result = bytearray(25 * 79)
param = array.array("f", (0.0, 2.0, 4.0, 0.0458, 0.08333))

@micropython.asm_thumb
def mandel(r0, r1):
    vldr(s10, [r1, 0])       # 0.0
    vldr(s11, [r1, 4])       # 2.0
    vldr(s12, [r1, 8])       # 4.0
    vldr(s13, [r1, 12])      # 0.0458
    vldr(s14, [r1, 16])      # 0.08333

    mov(r1, 0)               # calcCount
    mov(r4, 12)              # y
    neg(r4, r4)
    label(loop_y)
    vmov(s4, r4)
    vcvt_f32_s32(s4, s4)
    vmul(s4, s4, s14)        # cb = y * 0.083333
    mov(r3, 39)              # x
    neg(r3, r3)
    label(loop_x)
    vmov(s3, r3)
    vcvt_f32_s32(s3, s3)
    vmul(s3, s3, s13)        # ca = x * 0.0458
    vadd(s0, s3, s10)        # a = ca
    vadd(s1, s4, s10)        # b = cb
    vmul(s20, s0, s0)        # a*a
    vmul(s21, s1, s1)        # b*b
    mov(r5, 0)
    label(loop_i)
    add(r1, 1)
    vmul(s1, s0, s1)         # b *= a
    vmul(s1, s1, s11)        # b *= 2.0
    vadd(s1, s1, s4)         # b += cb
    vsub(s0, s20, s21)       # a = a*a - b*b
    vadd(s0, s0, s3)         # a += ca
    vmul(s20, s0, s0)        # a*a
    vmul(s21, s1, s1)        # b*b
    vadd(s22, s20, s21)      # a*a + b*b
    vcmp(s22, s12)           # a*a + b*b vs 4.0
    vmrs(APSR_nzcv, FPSCR)
    bgt(loop_i_exit)
    add(r5, 1)
    cmp(r5, 16)
    blt(loop_i)
    label(loop_i_exit)
    strb(r5, [r0, 0])
    add(r0, 1)
    add(r3, 1)
    cmp(r3, 40)
    blt(loop_x)
    add(r4, 1)
    cmp(r4, 13)
    blt(loop_y)
    mov(r0, r1)

gc.collect()
gc.disable()
t0 = time.monotonic_ns()
calcCount = mandel(result, param)
t1 = time.monotonic_ns()
gc.enable()
print(f"\n{(t1 - t0)*1e-3} us, calc count = {calcCount}")

tbl = "0123456789ABCDEF "
idx = 0
for y in range(-12, 13) :
    for x in range(-39, 40) :
        print(tbl[result[idx]], end = "")
        idx += 1
    print()
```

3.17 ms でした。float の掛け算が 1 clock で終わるので、さすがです。
