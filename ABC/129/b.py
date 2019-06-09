#b.py
n = int(input())
wli = list(map(int,input().split()))
ans = 10**8
for x in range(n):
    ans = min(ans,abs(sum(wli[:x])-sum(wli[x:])))
print(ans)
