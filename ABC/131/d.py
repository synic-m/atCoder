#d.py
n = int(input())
ab = [list(map(int,input().split())) for x in range(n)]
yes = True
time = 0
ab.sort(key=lambda x:x[1])
for x in ab:
    time += x[0]
    if time > x[1]:
        yes = False
        break
if yes:
    print('Yes')
else:
    print('No')
