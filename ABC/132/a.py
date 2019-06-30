#a.py
lis = []
s = input()
flag = 0
two = 0
for x in s:
    if x in lis:
        flag += 1
    else:
        two += 1
    lis.append(x)
if two == 2 and  flag <= 2:
    print('Yes')
else:
    print('No')
