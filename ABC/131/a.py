#a.py
s = input()
flag = True
bef = -1
for x in s:
    if x == bef:
        flag = False
    bef = x
if flag:
    print('Good')
else:
    print('Bad')
