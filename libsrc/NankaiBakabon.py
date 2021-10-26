#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 難解バカボンの Python への移植
# https://www.vector.co.jp/soft/dos/amuse/se007728.html
# 多少変更があります。
#
import re
from random import randint, randrange, choice

def remove_kugiri(txt) :
    return "".join(x for x in txt if x not in r"""[ !?:;.,^~_/<>()[\]{}「」。、・'"　！？：；．，。、・…‥＾＿／＜＞（）［］「」〔〕｛｝〈〉《》『』【】“”‘’]""")

inf4 = { "ください" : "いただき",
        }

inf3 = { "しない" : "せず",
         "はない" : "はなく",
         "がない" : "がなく",
         "にない" : "になく",
         "ている" : "ており",
         "でいる" : "でおり",
         "すぎる" : "すぎ",
         "さない" : "さず",
         "いない" : "おらず",
         "らない" : "らず",
         "えない" : "えず",
         "れない" : "れず",
         "せない" : "せず",
         "きない" : "きず",
         "しまう" : "しまい",
         "します" : "し",
         "います" : "おり",
         "得ない" : "得ず",
         "できる" : "でき",
        }

inf2 = { "する" : "し",
         "ずる" : "じ",
         "ある" : "あり",
         "える" : "え",
         "げる" : "げ",
         "ぜる" : "ぜ",
         "める" : "め",
         "れる" : "れ",
         "言う" : "言い",
         "いう" : "いい",
         "入る" : "入り",
         "見る" : "見て",
         "出る" : "出て",
         "得る" : "得て",
         "しい" : "しく",
         "あう" : "あい",
         "合う" : "合い",
         "せる" : "せ",
         "なる" : "なり",
         "した" : "し",
         "ない" : "なく",
         "ける" : "け",
         "です" : "で",
         "ます" : "",
         "ねる" : "ね",
         "とる" : "とり",
         "たい" : "たくて",
         "べる" : "べ",
         "てる" : "て",
        }

inf1 = { "だ" : "で",
         "く" : "き",
         "つ" : "ち",
         "む" : "み",
         "ぐ" : "ぎ",
         "ぶ" : "び",
         "う" : "い",
         "す" : "し",
         "い" : "く",
        }

# re_inf3 = re.compile( "(" + "|".join(inf3.keys()) + ")$" )
# re_inf2 = re.compile( "(" + "|".join(inf2.keys()) + ")$" )	# re_inf2.sub() causes freeze on CP6.1
# re_inf1 = re.compile( "(" + "|".join(inf1.keys()) + ")$" )

def inflect(txt) :
    if txt[-4:] in inf4 :
        txt = txt[:-4] + inf4[txt[-4:]]
    elif txt[-3:] in inf3 :
        txt = txt[:-3] + inf3[txt[-3:]]
    elif txt[-2:] in inf2 :
        txt = txt[:-2] + inf2[txt[-2:]]
    elif txt[-1:] in inf1 :
        txt = txt[:-1] + inf1[txt[-1:]]
    else :
        txt = txt + "し"
    return txt

class Word :
    dup_jt = [ "", "", "" ]     # 重複チェック
    prev   = ""                 # 直前の sel
    
    def __init__(self, type) :
        super().__init__()
        self.type = type
        self.pool = []          # a list of [ word, count ]
        self.dup  = ""          # 重複チェック
        self.wcheck = 0         # 重複チェック

    def add(self, word) :
        self.pool.append([ word, 0 ])

    def update(self, rc) :
        self.wcheck = min(255, len(self.pool) * rc // 10)

    def dec_counter(self) :
        for a in self.pool :
            if a[1] > 0 : a[1] -= 1
        
    def sel(self) :
        # if len(self.pool) <= 0 : return ""
        dup_check = 15          # 重複チェック上限
        while dup_check > 0 :
            a = choice(self.pool)
            if a[1] > 0 :
                a[1] -= 1
                continue

            # 例外処理
            w = a[0]

            if len(w) >= 4 and self.prev.endswith("い") :       # 直前が形容詞
                if re.match("^(べか|べき|べく|べし|しか|ため|には|まで)", w) : continue

            dup_check -= 1
            if self.type == 5 :         # 接続助詞の重複チェック
                tmp = remove_kugiri(w)[-2:]
                if tmp == self.dup : continue
                self.dup = tmp

            if self.type == 6 :         # 文末句の述語語尾の重複チェック
                tmp = w[-2:]
                if tmp == self.dup or tmp in self.dup_jt : continue
                self.dup = w[-2:]

            if self.type == 3 or self.type == 4 :
                self.dup_jt.pop(0)
                self.dup_jt.append(w[-2:])

            # 直前の語句との比較による重複チェック
            if any( x in self.prev and x in w
                    for x in ("であ", "され", "とい" ,"と言", "でき", "もの") ) : continue

            break
        
        self.set_prev(a[0])
        a[1] = self.wcheck

        return a[0]
            
    @classmethod
    def set_prev(cls, word) :
        cls.prev = word

class NankaiBakabon :
    def __init__(self, fname = None) :
        """Set up NankaiBakabon by reading dictionary."""
        super().__init__()
        self.mn = 1             # 一文の長さ(最小)                              
        self.mx = 5             # 一文の長さ(最大)                              
        self.sn = 6             # 一段落あたりの文の個数(1-32000)               
        self.rc = 2             # 同一語句の重複チェックをどの程度するか(0-10)  
        self.sc = 60            # 主語を省略する割合(0-100)                     
        self.sh = 70            # 副詞句を省略する割合(0-100)                   
        self.jt = 50            # 全述語のうち他動詞句の割合(0-100)             
        self.sz = 50            # 接続句で文と文を接続する割合(0-100)           
        self.bm = 50            # 文末句で文を終わらせる割合(0-100)             
        self.kuten = "。"       # 句点
        self.toten = "、"       # 読点

        # 0: 名詞句
        # 1: 主語につく助詞
        # 2: 副詞句
        # 3: 自動詞句（自動詞・形容詞・形容動詞）
        # 4: 他動詞句（助詞＋他動詞）
        # 5: 接続句
        # 6: 文末句
        self.word = [ Word(i) for i in range(7) ]

        if fname : self.read_dict(fname)

    def read_dict(self, fname) :
        """Append dictionary."""
        idx = 0
        with open(fname) as f :
            for l in f :
                if l.startswith("\n") : continue
                if l.startswith("'")  : continue
                if l.startswith("-") or l.startswith("/") :
                    self.set_opt(l)
                    continue
                if l.startswith("@") :
                    idx += 1
                    if idx >= 7 : break
                    continue
                self.word[idx].add(l.rstrip("\n"))
        if idx != 7 : raise ValueError("Invalid dictionary: " + fname)
        if self.mn > self.mx : raise ValueError("Wrong parameter in dictionary: " + fname)
        for w in self.word : w.update(self.rc)

    def set_opt(self, l) :
        opt = l[1:3].lower()

        if opt == "kt" :
            self.kuten = re.match(r'"(.*)"', l[3:]).group(1)
            return
        if opt == "tt" :
            self.toten = re.match(r'"(.*)"', l[3:]).group(1)
            return

        val = int(l[3:].split()[0])
        if opt == "mn" :   self.mn = max(1, min(100, val))
        elif opt == "mx" : self.mx = max(1, min(100, val))
        elif opt == "sn" : self.sn = max(1, min(32000, val))
        elif opt == "rc" : self.rc = max(0, min(10, val))
        elif opt == "bm" : self.bm = max(0, min(100, val))
        elif opt == "sc" : self.sc = max(0, min(100, val))
        elif opt == "sh" : self.sh = max(0, min(100, val))
        elif opt == "sz" : self.sz = max(0, min(100, val))
        elif opt == "jt" : self.jt = max(0, min(100, val))
        else :
            raise ValueError("Invalid option: " + l)

    def sentence(self, words = None) :
        """Return a nankai sentence as str.  If words = [...] is given, a
        sequence of nankai words are appended to the list.

        """
        slen = randint(self.mn, self.mx)                # 一文の長さ
        
        txt = [] if words is None else words
        st  = True              # '文の先頭'を示す

        for i in range(slen + 1) :
            # 副詞句その１
            if randrange(100) > self.sh : txt.append(self.word[2].sel())
            
            # 主語と助詞
            if randrange(100) > self.sc  or  st:
                st = False
                txt.append(self.word[0].sel())
                txt.append(self.word[1].sel())

            # 副詞句その２
            if randrange(100) > self.sh : txt.append(self.word[2].sel())

            # 述語節
            if randrange(100) < self.jt :
                txt.append(self.word[3].sel())  # 自動詞
            else :
                txt.append(self.word[0].sel())  # 目的語
                txt.append(self.word[4].sel())  # 他動詞

            if i >= slen : break
            
            # 文の接続
            if randrange(100) < self.sz :
                txt.append(self.word[5].sel())  # 接続句
            else :
                txt.append(inflect(txt.pop()))  # 語形変化
                txt.append(self.toten)

        # 文末処理
        if randrange(100) < self.bm :
            txt.append(self.word[6].sel())
        txt.append(self.kuten)

        for w in self.word : w.dec_counter()

        return "".join(txt) if words is None else words

    def paragraph(self, words = None) :
        """Return a nankai paragraph as str, starting with a zenkaku space
        (without trailing '\n').  When words = [...] is given, a
        sequence of nankai words are appended to workds, as well as
        '\n'.
        
        """
        para = [] if words is None else words
        para.append( "　" )
        for _ in range(self.sn) : self.sentence(para)
        if words is None :
            return "".join(para)
        else :
            para.append("\n")
            return para

        
#------------------------------------------------------------------------
if __name__ == "__main__" :
    import sys

    nanba = NankaiBakabon()

    n = 5
    if sys.argv[-1].isdigit() :
        n = int(sys.argv.pop())
        
    for fname in sys.argv[1:] :
        nanba.read_dict(fname)

    for _ in range(n) :
        print(nanba.paragraph())
