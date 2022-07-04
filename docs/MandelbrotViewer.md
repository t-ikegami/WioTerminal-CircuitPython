# マンデルブロビューワ

## 概要
こちらの~~パクリ~~劣化移植。<br/>
https://github.com/shapoco/picosys-mandelbrot <br/>
高速化の工夫を放棄して FPU をぶんまわしています。
実行には native を有効にした[カスタムファームウェア](/Firmware/MyCircuitPython7.3.uf2) が必要です。

## ファイル
   [`Mandelbrot.py`](/CIRCUITPY/Mandelbrot.py)

## 操作
- ←→↑↓ : 表示範囲を移動します。
- 3 2 : 拡大・縮小します。
- X : 中心点をコンソールに出力します。

