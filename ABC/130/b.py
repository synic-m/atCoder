#b.py
n,x = map(int,input().split())
lis = list(map(int,input().split()))

ans = 1
now = 0
for _ in lis:
    now += _
    if x >= now:
        ans += 1
    else:
        break
print(ans)
