H,W=map(int,input().split())
field=[input() for x in range(H)]

lis = [[  for x in range(W) if field[y][x] == '#']for y in range(H)]
print(lis)
vy=[0,0,1,-1]
vx=[1,-1,0,0]

i=0
if len(lis) == 1:
    i = 1
flag = -1
def change(lis):
    global i,flag
    while lis:
        if abs(flag-len(lis))>2:
            i+=1
        flag = len(lis)
        y,x = lis.pop(0)
        for dy,dx in zip(vy,vx):
            ny,nx = y+dy,x+dx
            if 0<=ny<H and 0<=nx<W:
                if field[ny][nx] == '.':#.
                    field[ny][nx] = '#'
                    lis.append([ny,nx])
                
    return i
print(change(lis))
