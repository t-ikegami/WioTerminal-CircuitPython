# 準備

- CircuitPython は以下より取得します。<br/>
  https://circuitpython.org/board/seeeduino_wio_terminal/ <br/>
  7.0.0 で検証しています。
- 無線通信のファームウェアを 2.1.3_JP にアップデートします。<br/>
  https://wiki.seeedstudio.com/Wio-Terminal-Network-Overview <br/>
- 外部ライブラリを使用します。<br/>
  https://circuitpython.org/libraries
  より
  adafruit-circuitpython-bundle-7.x-mpy-*.zip
  を取得します。以下のライブラリを使うので、必要に応じて lib 以下にコピーします。
  ```
  adafruit_imageload/
  adafruit_lis3dh.mpy
  adafruit_hid/
  adafruit_miniqr.mpy
  ```
  また、以下のデータを CIRCUITPY 直下にコピーします。
  ```
  examples/font5x8.bin
  ```
