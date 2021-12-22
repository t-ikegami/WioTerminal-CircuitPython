# ファームウェア

Wio Terminal 向け CircuitPython 7.0.0 に以下の修正を加えました。

- `_bleio` を削除
- `uzlib` を追加
- `stage` を追加
- シリアルコンソールは EMACS Key 対応

[ネイティブコードエミッター](https://micropython-docs-ja.readthedocs.io/ja/latest/reference/speed_python.html#the-native-code-emitter) を有効にしたものも置いておきます。こちらは `stage` は入っていません。