n = int(input())
h = list(map(int,input().split()))
ans = 0
flag = False
while sum(h) > 0:
    ans += 1
    print(ans)
    flag = False
    for x in range(n):
        if h[x] > 0:
            h[x] -= 1
            print(h)
            flag = True
        elif flag is True:
            break
print(h)
print(ans)
