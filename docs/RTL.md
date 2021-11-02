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

## 問題点
いくつかの Web site に WiFiClientSecure で接続できません。
`ssl.start_client` が `-0x7280:CONN_EOF` で失敗します。
暗号化スイート `ECDHE-RSA-AES256-GCM-SHA384` が選択されると、失敗するように見えます。
ライブラリに不備があり、設定すべき項目を見逃しているのかもしれません。
何かお気づきの点がございましたら、ご一報いただけると幸いです。

テスト用スクリプトを `test_WiFiClientSecure` 以下に置いておきます。
- 成功例 : `test_secure.py`
- 失敗例 : `test_tenki.py`

