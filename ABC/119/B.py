N = int(input())
X =[]
ans = 0
for _ in range(N):
    X.append(input().split())
    X[_][0] = float(X[_][0])
    if X[_][1] == 'BTC':
        X[_][0] = X[_][0] * 380000
    ans += X[_][0]
#print(X)
print(ans)
