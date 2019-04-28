N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
for x in range(N):
    if V[x] > C[x]:
        ans += (V[x]-C[x]) 
print(ans)
