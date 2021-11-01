# ピクセルエディタ

## 概要
ピクセル画像を表示・編集します。
ドットの色は 16 色で、サイズは 8x8, 11x11, 16x16 の 3 通り用意しました。

[![YouTube](./Pixel.jpg)](https://www.youtube.com/watch?v=6AHvsP6kS2U)

## ファイル
   `pixel*.py`, `pixel*.dat`

## ライブラリ
   `PixelDisplay.mpy`, `Cursor.mpy`

## 操作
サムネール画面:
- ↑↓←→ : カーソル移動
- "2" : 選択したサムネール画像をエディタに送る。
- "3" : エディタの画像をサムネールに登録する。
- "1" : 終了

エディタ画面:
- ↑↓←→ : カーソル移動
- "X" : セット・pen down/up
- "2", "3" : ペンの色を変更
- "1" : サムネール画面へ

終了時に画像データがダンプされます。
シリアルコンソールから `import pixel` のように起動し、
上記ダンプデータを 'pixel*.dat` ファイルに保存することで、次回起動時に反映することができます。
データは自動的には save されません。
https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage




