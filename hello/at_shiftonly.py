N = input()
A = list(map(int,input().split()))
N_flag = 0
flag = True
A_judge = list(map(lambda x: x%2,A))
while flag == True:
    if A_judge.count(1) == 0:
        A = list(map(lambda y: y/2,A))
        A_judge = list(map(lambda x: x%2,A))
        N_flag += 1
    else:
        flag = False
print(N_flag)

