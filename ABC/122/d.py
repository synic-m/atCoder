N,mod = int(input()),10**9+7

w = "ATCG"

table = []
for _1 in w:
    for _2 in w:
        for _3 in w:
            table[_1+_2+_3] = 1


NG = ['AGC','ACG','GAC']
for ng in NG:
    table = 0

for i in range(N-3):
    t = table.copy()
    for _1 in w:
        for _2 in w:
            for _3 in w:
                s = _1 + _2 + _3
                if s in NG:
                    continue

                if _1 == 'G' and _3 == 'C' or _2 == 'G' and _3 == 'C':
                    res = 0
                    for _4 in "TCG":
                        ss = _4 + _1 + _2
                        res += table[ss]
                    t[s] = res
                    continue
                res = 0
                for _4 in w:
                    ss = c4 + c1 + c2
                    res += table[ss]
