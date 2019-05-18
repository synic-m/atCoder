#bfs 
#0#000  1#100 1#120 1#123
#00000  01010 21212 21212
#000#0  001#1 021#1 321#1
#000#0  001#1 021#1 321#1

from collections import deque

h,w = map(int,input().split())
lis = [input() for x in range(h)]

vy = [0,0,1,-1]
vx = [1,-1,0,0]

reached = [[-1]*w for x in range(h)]
def bfs(bk_lis):
    q = deque()
    for i in bk_lis:
        q.append(i)
        reached[i[0]][i[1]]=0
    while q:
        y,x = q.popleft()
        for dy,dx in zip(vy,vx):
            ny,nx = y+dy,x+dx
#                print(ny,nx)
            if not(0<=ny<h and 0<=nx<w):
                continue#範囲の確認
            if  reached[ny][nx]==-1 or reached[ny][nx]>reached[y][x]+1:
                reached[ny][nx] = reached[y][x]+1
                q.append([ny,nx])
#        print(reached)
bk_lis = []
ans=0
for y in range(h):
    for x in range(w):
        if lis[y][x] == '#':
            bk_lis.append([y,x])
#print(bk_lis)
bfs(bk_lis)
for y in reached:
    ans = max(max(y),ans)
#for x in reached:
#    print(x)
print(ans)
