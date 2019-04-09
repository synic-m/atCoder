N = int(input()) 
txy = [list(map(int,input().split())) for x in range(1,N+1)]       
txy = [[0,0,0]] + txy
####print(txy)
t = 0
###print(txy)
for _ in range(1,N+1):
    #print(_)
    #print(txy[0])
    t = txy[_][0] - txy[_-1][0]
    chan_x = txy[_][1] - txy[_-1][1] 
    chan_y = txy[_][2] - txy[_-1][2]
    #print(chan_y,chan_x ,"chan_x,chan_y")
    if t < abs(chan_y) + abs(chan_x):
        flag = False
    elif t == abs(chan_x) + abs(chan_y):
        flag = True
    elif t > abs(chan_y) + abs(chan_x):
        if (abs(chan_x)+abs(chan_y))%2 == 0 and t%2 ==0:
            flag = True
        elif (abs(chan_x)+abs(chan_y))%2 == 1 and t%2 == 1:
            flag = True
        else:
            flag = False

if flag == True:
    print('Yes')
else:
    print('No')
