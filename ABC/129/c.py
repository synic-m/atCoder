#c.py
mod = 10**9 + 7
import sys
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())
alis = [int(input()) for x in range(m)]
ans = 0
def dfs(N):
    global ans
    if N > n:
        return
    if N in alis:
        return
    if N == n:
        ans += 1
        return
    #print(N)
    dfs(N+1)
    dfs(N+2)
dfs(0)
print(ans)
