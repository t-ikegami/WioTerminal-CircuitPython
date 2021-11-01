# ネットワーク接続

## 概要
こちらの~~パクリ~~移植。<br/>
https://github.com/Seeed-Studio/Seeed_Arduino_rpcUnified

RTL8720 と UART 経由で [eRPC](https://github.com/EmbeddedRPC/erpc) 通信するライブラリです。
Bluetooth 系も実装してありますが、未検証です。(RTL8720 からのコールバックで raise します。)

![RTL8720](./RTL.jpg)

## ライブラリ
   `wio_terminal_rtl/*`

## 操作
```
from wio_terminal_rtl.rpc import system
system.version()
```
