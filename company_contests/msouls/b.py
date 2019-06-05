s = input()
cnt = 0
for x in s:
    if x == 'x':
        cnt += 1
if cnt < 8:
    print('YES')
else :
    print('NO')
