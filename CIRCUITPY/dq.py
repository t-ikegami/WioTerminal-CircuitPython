import board
import displayio  as dpio
from ButtonEvents import ButtonEvents
import time
from random import choice
from RictyBoldTerminal import RictyHTerminal

dq = [
    "もしわしのみかたになれば、せかいのはんぶんをやろう。",
    "しんでしまうとはなにごとだ！",
    "へんじがない　ただのしかばねのようだ。",
    "ゆうべはおたのしみでしたね。",
    "そんな　ひどい・・・",
    "いやー、さがしましたよ。",
    "ぎょえーっっ！",
    "なにゆえもがきいきるのか？ほろびこそわがよろこび。しにゆくものこそうつくしい。さあわがうでのなかでいきたえるがよい！",
    "ゆるしてくれよ！な！な！",
    "そして　でんせつがはじまった！",
    "そしてよがあけた。",
    "ぼくわるいすらいむじゃないよ",
    "おことばですが、おうさま。",
    "ひきあげじゃあ！",
    "ぬわーーっ！！",
    "ぼうや、どんなつらいことがあっても、まけちゃだめだよ。",
    "なんと。このわたしがすきともうすか！？",
    "なんだかねむれなくて・・・",
    "５０ねんのつきひは・・・あまりにながすぎた。",
    "ゆめよりもはるかにおそろしい、げんじつというものをみせてやろう。",
    "おろかものめ！いしとなり、えいえんのときをくやむがよい！",
    "すーぷさめた。つくりなおし・・・",
    "あそんでくれてありがとう。つまらなかったわ。",
    "そ　こ　に　あ　っ　た　の　か",
    "きゃっ、こっちみないでよ！このえっちまん！",
    "それ　いいすぎ。",
]

disp = board.DISPLAY
term = RictyHTerminal(15, 10)
term.x = 10
term.y = 20
disp.show(term)

def show(term, txt, delay = 0.1) :
    n = len(txt)
    if (n <= 15) :
        x = (15 - n) // 2 + 1
        y = 5
    else :
        x = 1
        y = 5 - (len(txt)-1) // 30
    term.write(f"\x1b[2J\x1b[{y};{x}H")
    for x in txt :
        term.write(x)
        time.sleep(delay)

be = ButtonEvents()

b = 0
while True :
    txt = choice(dq)
    show(term, txt)
    
    t = time.monotonic()
    while b : b = be.get_pressed()	# wait until key release
    while b == 0 and time.monotonic() - t < 5 :
        time.sleep(0.1)
        b = be.get_pressed()
    if b & be.K_SELECT : break

be.deinit()
disp.show(None)
