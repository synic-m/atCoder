n,m = map(int,input().split())
alis = sorted(list(map(int,input().split())))
BC = []
clis = []

for x in range(m):
    b,c = map(int,input().split())
    BC.append((b,c))

BC = sorted(BC,reverse=True,key=lambda x:x[1])


bk_flg = 1
for b,c in BC:
    for x in range(b):
        if len(clis) > n:
            bk_flg = 0
            break
        clis.append(c)
    if bk_flg == 0:break;

for i in range(min(len(clis),n)):
    if alis[i] < clis[i]:
        alis[i] = clis[i]
print(sum(alis))
