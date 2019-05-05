from collections import deque

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())

vy = [0,0,1,-1]
vx = [1,-1,0,0]

maze = [input() for _ in range(R)]
reached = [[-1]*C for _ in range(R)]
#print(R,C,'\n',sy,sx,':start',gy,gx,':goal')
#for x in maze:
#    print(x)
def bfs(y,x):
    q = deque([[y,x]])
    reached[y][x] = 0
   # print(reached)
    while q:
        y,x = q.popleft()
        if [y,x] == [gy-1,gx-1]:
            return reached[y][x]
        for dy,dx in zip(vy,vx):
            ny,nx = y+dy,x+dx
            if not(0<= ny < R and 0<= nx < C):
                continue
            if maze[ny][nx] == '.' and reached[ny][nx] == -1:
                reached[ny][nx] = reached[y][x] + 1
                q.append([ny,nx])
print(bfs(sy-1,sx-1))
