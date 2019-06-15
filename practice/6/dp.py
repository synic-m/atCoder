n = int(input())
h = list(map(int,input().split()))

ans = 0
skip = False
for x in range(n-1):
    if skip:
        skip = False
        continue
    ans += min(abs(h[x+1]-h[x]),abs(h[x+2]-h[x]))
    if abs(h[x+1]-h[x])<abs(h[x+2]-h[x]):
        skip = True
print(ans)

