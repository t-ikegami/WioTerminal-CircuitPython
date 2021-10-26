import re
from random import choice

class Sentence :
    pat = re.compile(r"w(\d+)(=?)")

    def __init__(self, fname) :
        super().__init__()
        
        W = [[] for _ in range(10)]
        with open(fname) as f :
            self.title = f.readline().rstrip("\n")
            for l in f :
                if l.startswith("--") : continue
                if l.startswith("*w") :
                    w = W[int(l[2])]
                    continue
                if l.startswith("*end") : break
                l = l.rstrip("\n")
                l = re.sub(r"\\n", "\n", l)
                w.append(l)
            self.comment = "".join(f.readlines())
        self.W = W

    def sentence(self) :
        tmp = choice(self.W[0])
        ph = dict()	# placeholder for w.*=
        while True :
            m = self.pat.search(tmp)
            if m is None : break
            lst = []
            for i in m.group(1) : lst.extend(self.W[int(i)])
            if m.group(2) :
                s = ph[m.group(1)]
            else :
                s = choice(lst)
                ph[m.group(1)] = s
            tmp = self.pat.sub(s, tmp, 1)
        return tmp
        
#------------------------------------------------------------------------
if __name__ == "__main__" :
    import sys
    from Sentence import Sentence

    n = 1
    sen = Sentence(sys.argv[1])
    if len(sys.argv) > 2 : n = int(sys.argv[2])

    for i in range(n) :
        print(sen.sentence())
        print()

