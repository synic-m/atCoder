import sys
from collections import deque

sys.setrecursionlimit(100000)

H,W = map(int,input().split())
start = list(map(int,input().split()))
goal = list(map(int,input().split()))
maze = [input() for x in range(H)]
reached = [[1000 for x in range(W)]for y in range(H)]

vy = [0,0,1,-1]
vx = [1,-1,0,0]

q = deque()
def bfs(s,g):
    q.append(s)
    reached[s[1]][s[0]] = 0
    while q:
        y,x = q.popleft()
        #print(y,x,'     q')
        if [y,x] == g:
            #print('goal',g,[y,x])
            return reached[y][x]
        
        for dy,dx in zip(vy,vx):
            ny,nx = y+dy,x+dx
            #print(ny,nx,'      vect',dy,dx)
            if maze[ny][nx] == '#':
                #print('#')
                continue
            if reached[ny][nx] != 1000:
                #print('1-1-1')
                continue
            reached[ny][nx] = reached[y][x]+1
            q.append([ny,nx])
#            print(q)
print(bfs([start[0]-1,start[1]-1],[goal[0]-1,goal[1]-1]))
#for x in reached:
#    print(x)
