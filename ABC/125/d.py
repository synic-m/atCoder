n = int(input())
a = list(map(int,input().split()))
an = list(map(abs,a))
cnt=0
for x in range(n):
    if a[x] < 0:
        cnt += 1

if cnt%2 == 0:
    print(sum(map(abs,a)))
else:
    print(sum(map(abs,a)) - 2*min(an))
