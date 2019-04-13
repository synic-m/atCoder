N = int(input())

lis = list(map(int,input().split()))
ans = 0
flag = lis[0]
for x in lis:
    if flag > x:
        continue
    ans += 1

    if flag < x:
        flag = x
print(ans)
