N,Y = map(int,input().split())
flag = False
for x in range(N+1):
    t_t = x
    for y in range(N+1 - x):
        f_t = y
        o_t = (N -x -y)
        if Y == 10000*t_t + 5000*f_t + 1000*o_t:
            #print(Y,'ttftot = ',t_t,f_t,o_t)
            flag = True
            break
    if flag == True:
        break
if flag == True:
    print(t_t,f_t,o_t)
else :
    print(-1,-1,-1)
