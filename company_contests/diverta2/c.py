#c.py
n = int(input())
lis = list(map(int,input().split()))
lis.sort()
m = lis[0]
M = lis[-1]
ans_lis = []

for now in lis[1:-1]:
    if now > 0:
        ans_lis.append([m,now])
        m -= now
    else:
        ans_lis.append([M,now])
        M -= now
ans_lis.append([M,m])
print(M-m)
for x in ans_lis:
    print(x[0],x[1])
