import sys
sys.setrecursionlimit(1000000)
H,W = map(int,input().split())
MAP = [input() for x in range(H)]
reach = [[False for y in range(W)] for x in range(H)]
for y in range(H):
    for x in range(W):
        if MAP[y][x] == 's':
            s = [y,x]
        elif MAP[y][x] == 'g':
            g = [y,x]
def serch_root(x,y):
    if x < 0 or y < 0 or x >= H or y >= W:
        return
    if MAP[x][y] == '#' or reach[x][y] == True:
        return 
    reach[x][y] = True
    serch_root(x+1,y)
    serch_root(x-1,y)
    serch_root(x,y+1)
    serch_root(x,y-1)

serch_root(s[0],s[1])
print('Yes' if reach[g[0]][g[1]] else 'No')

