n,m = map(int,input().split())
lis = [int(input()) for x in range(m)]
flag = True

for x,y in zip(lis,lis[1:]):
    if x == y:
        flag = False
        break
ans = 1
bef = 0
for no in lis:
    x = no-bef
    ans *= 2**(x-1)//2
    bef = no
ans *= 2**(x-1)//2


mod = 10**9 + 7

if flag:
    print(ans%mod)
else:
    print(0)
