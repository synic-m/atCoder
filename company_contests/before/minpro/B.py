flag = 0
a = []
for x in range(3):
    a +=list(map(int,input().split()))
if a.count(1) == 2:
    flag += 1
if a.count(2) == 2: 
    flag += 1
if a.count(3) == 2:
    flag += 1
if a.count(4) == 2:
    flag += 1
if flag == 2:
    print('YES')
else:
    print('NO')
