n,m = map(int,input().split())
alis = sorted(list(map(int,input().split())))
lis = []
clis = []
for x in range(m):
    b,c = map(int,input().split())
    lis.append((b,c))
lis = sorted(lis,reverse=True,key=lambda x:x[1])
for b,c in lis:
    for _ in range(b):
        if len(clis) > n:
            break
        clis.append(c)
    else:
        continue
    break
l = len(clis)
ans = 0
for x,y in zip(alis,clis):
    ans += max(x,y)

if n>l:
    ans += sum(alis[l:])
print(ans)
