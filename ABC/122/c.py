N,Q = map(int,input().split())
S = input()
lr = [list(map(int,input().split())) for _ in range(Q)]
flag = False
q_flag = []
count = 0
for x in S:
    count += 1
    if x == 'A':
        flag = True
    elif x == 'C' and flag == True:
        flag = False
        q_flag.append(count)
    else:
        flag = False
print(q_flag)
for y in lr:
    ans = len([_1 for _1 in q_flag if y[0]<_1 and _1<=y[1]])
    print(ans)
