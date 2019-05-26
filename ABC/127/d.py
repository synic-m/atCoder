n,m = map(int,input().split())
alis = list(map(int,input().split()))
clis = [[[int(x)]*int(y) for x,y in zip(input().split())]for z in range(m)]
clis.sort(reverse=True)
l = len(clis)
alis.sort()
ans = 0
for x,y in zip(alis,clis):
    ans += max(x,y)
if n>l:
    ans += sum(alis[l:])
print(ans)
