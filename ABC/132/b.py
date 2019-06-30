#b.py
n = int(input())
lis = list(map(int,input().split()))
ans = 0
for x,y,z in zip(lis,lis[1:],lis[2:]):
    if x < y < z or z < y < x:
        ans += 1
print(ans)
