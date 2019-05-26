n,m = map(int,input().split())
ks = [list(map(int,input().split())) for x in range(m)]
plis = list(map(int,input().split()))
ans = 0
llis=[]
for x in range(2**n):
    sw_lis = [0]*n
    for y in range(n):
        if ((x >> y)&1):
            sw_lis[y] = 1
    llis.append(sw_lis)
for sw in llis:
    judge = 0
    on = 0
    for x in range(m):
        for i in ks[x][1:]:
            judge += sw[i-1]
        if judge%2 == plis[x]:
            on += 1    
            judge = 0
    if on == m:
        ans += 1
print(ans)
