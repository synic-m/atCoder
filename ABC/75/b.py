da = [0,0,-1,-1,-1,1,1,1]
db = [-1,1,-1,0,1,-1,0,1]

h,w = map(int,input().split())
lis = [input() for x in range(h)]
ans_lis = [[0 for x in range(w)] for y in range(h)]

def cnt(y,x):
    if y >= h or x >= w or y < 0 or x < 0:
        return 0
    if lis[y][x] == '#':
        return 1
    return 0

for y in range(h):
    for x in range(w):
        ans = 0
        if lis[y][x] == '.':
            for dx,dy in zip(da,db):
                ans += cnt(y+dy,x+dx)
            ans_lis[y][x] = str(ans)
        else:
            ans_lis[y][x] = '#'
for x in range(h):
    print(''.join(ans_lis[x]))
