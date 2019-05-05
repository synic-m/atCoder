H,W = map(int,input().split())
field = [input() for x in range(H)]
vx = [0,0,1,-1]
vy = [1,-1,0,0]
reached = [[-1 for x in range(W)]for x in range(H)]
from collections import deque
def bfs(y,x):
    q = deque([[y,x]])
    reached[y][x] = 1

    while q:
        y,x = q.popleft()
        if [y,x] == [H-1,W-1]:
            return reached[y][x]
        for dy,dx in zip(vy,vx):
            ny,nx = y+dy,x+dx
            if not (0<=ny<H and 0<=nx<W):
                continue
            if field[ny][nx] == '.' and reached[ny][nx] == -1:
                q.append([ny,nx])
                reached[ny][nx] = reached[y][x] + 1
    return -1
bk = 0
for x in field:
    for y in x:
        if y == '#':
            bk += 1
ans = bfs(0,0)
if ans==-1:
    print(-1)
else:
    print(H*W-ans-bk)
