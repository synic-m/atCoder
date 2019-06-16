#d.py
import sys
n,k = map(int,input().split())
a = [0]
a += list(map(int,input().split()))
ans = 0
bef = sum(a)
cnt = -1
if bef < k:
    print(0)
    sys.exit()
elif bef == k:
    print(1)
    sys.exit()
for num in a:
    cnt += 1
    M = bef - num
    bef = M
    for x in a[-1:cnt:-1]:
        if M >= k:
            ans += 1
        else:
            break
        M -= x
print(ans)

