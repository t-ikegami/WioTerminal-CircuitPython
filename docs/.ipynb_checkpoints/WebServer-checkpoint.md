# WEB サーバ

## 概要
こちらの~~パクリ~~移植。<br/>
https://lab.seeed.co.jp/entry/2021/05/11/120000

Wio Terminal 上にアクセスポイントを立て、そこで Web Server を走らせます。
当該 Web ページにアクセスすることで、Wio Terminal の LED を ON/OFF します。

[![YouTube](./WebServer.jpg)](https://www.youtube.com/watch?v=K_zljt7O878)

## ファイル
   `Lchika_AP.py`

## ライブラリ
   `wifi_start_ap.mpy`

## 操作
SSID "Lchika_AP", Password "Wio Terminal" でアクセスポイントに接続します。
ブラウザから http://192.168.1.1 にアクセスすると、LED を ON/OFF できます。

