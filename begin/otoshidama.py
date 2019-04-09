N,Y = map(int,input().split())
flag = False
ans_x = -1
ans_y = -1
ans_z = -1
for x in range(N+1):
    for y in range(N+1-x):
        sum_a = 10000*x
        sum_a += 5000*y
        sum_a += 1000*(N-x-y) 
        if Y == sum_a:
            flag = True
            break
    if flag == True:
        ans_x = x
        ans_y = y
        ans_z = N-x-y
        break
#print('x',x)
#print('N',N)
#print('sum_a',sum_a)
print(ans_x,ans_y,ans_z)

