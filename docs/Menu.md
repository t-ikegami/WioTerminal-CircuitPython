# メニュー表示

## 概要
こちらの~~パクリ~~移植。<br/>
https://github.com/pypewpew/game-m4-menu

`*.py` ファイルを選択して実行 (import) します。
起動時に RTL8720 を disable して消費電流を削減します。(平常時 5 V 100 mA が 70 mA になります。)
起動したアプリケーションが終了すると、自動的にソフトリセットがかかり、復帰します。

[![YouTube](./Menu.jpg)](https://www.youtube.com/watch?v=ZSyzFWfQR3k)

## ファイル
   [`main.py`](/CIRCUITPY/main.py)

## ライブラリ
   [` Menu.mpy`](/libsrc/Menu.py), [`wio_terminal_rtl/__init__.mpy`](/libsrc/wio_terminal_rtl/__init__.py)

## 操作
CIRCUITPY ドライブ上の code.py 等を削除し、
シリアルコンソールから Ctrl-D でソフトリセットすると、メニューが起動します。
↑↓←→で選択し、"X" で実行。終了するには "1" を押します。
