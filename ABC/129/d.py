#d.py
h,w = map(int,input().split())
slis = [input() for x in range(h)]
vy = [0,0,1,-1]
vx = [1,-1,0,0]

ans_lis = []
ma = 0
for ny in range(h):
    bef = 0
    y = slis[ny]
    cnt = 0
    lis = []
    for x in range(w):
        if y[x] == '.':
            cnt += 1
        elif y[x] == '#':
            if ma < cnt:
                ma = cnt
                ma_fla = x
                ma_bef = bef+1
            bef = x
            cnt = 0
    else:
        lis.append(cnt)
        if ma < cnt:
            ma = cnt
            ma_fla = x
            ma_bef = bef+1
ans = ma_fla - ma_bef
y_as = 0
for y in range(ma_bef,ma_fla):
    cnt = 0
    for x in range(h):
        ar = slis[x][y]
        if ar == '.':
            cnt += 1
        elif ar == '#':
            if y_as < cnt:
                y_as = cnt
            cnt = 0
    if y_as < cnt:
        y_as = cnt
ans += y_as      
#print('ans')
print(ans)
#print('len','#','#')
#print(ma,ma_bef,ma_fla)
#print(y_as)
