#file a.py
lis = [int(input()) for x in range(5)]
k = int(input())

for _ in range(1,5):
    for x in range(5-_):
        ans_flag = lis[x] - lis[_]

        if abs(ans_flag) > k:
            flag = 0
        else:
            flag = 1

if flag == 0:
    print(':(')
else :
    print('Yay!')
