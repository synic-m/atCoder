n = int(input())
lis = sorted(list(map(int,input().split())))
now = -1
ans = 0
for x in range(n):
    if lis[x] == now:
        continue
    now = lis[x]
    val = 0
    for y in range(n-x):
        if lis[x]+2 >= lis[x+y]:
            val += 1
            ans = max(ans,val)
        else:
            break

print(ans)
