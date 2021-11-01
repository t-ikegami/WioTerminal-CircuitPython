# 天気予報

## 概要
こちらの劣化~~パクリ~~移植。<br/>
https://github.com/99yen/WioTerminal-WeatherSign

Yahoo! の rss に HTTPS 接続して天気情報を取得し、表示します。
地域を変更するには、39 行目の `*.xml` 指定を調整します。

[![YouTube](./Weather.jpg)](https://www.youtube.com/watch?v=U0EXut60uTI)

## ファイル
   `weather.py`

## 問題点
当初、tenki.jp への接続を試みましたが、うまくいきませんでした。
`start_ssl_client` が通りません。
暗号化スイート `ECDHE-RSA-AES256-GCM-SHA384` が選択されると、失敗するようです。
何か設定すべき項目を見逃しているのかもしれません。
