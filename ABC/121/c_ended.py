N,M = map(int,input().split())

AB = [list(map(int,input().split())) for i in range(N)]
AB.sort()
ans = 0
for _ in range(N):
    if AB[_][1] >= M:
        ans += AB[_][0]*M
        break
    else:
        ans += AB[_][0]*AB[_][1]
        M -= AB[_][1]
print(ans)
