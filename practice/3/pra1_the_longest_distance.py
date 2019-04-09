N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for y in range(N):
    for x in range(N):
        _max = (((xy[y][0] - xy[x][0] )** 2) + ((xy[y][1] - xy[x][1]) ** 2)) ** (1/2)
        if _max > ans:
            ans = _max

print(ans)
