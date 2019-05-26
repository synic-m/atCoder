n,k = map(int,input().split())
v = list(map(int,input().split()))

ans = 0

for l in range(n):
    #左から何個取るか
    for r in range(n-l+1):
        #右から何個取るか
        if l+r >k:
            break
        nv = v[:l] + v[n-r:]
        nv.sort()
        for i in range(k-l-r):
            #負数をpop
            if not nv or nv[0] >= 0:
                break
            nv.pop(0)
        #最大値をansにする
        ans = max(ans,sum(nv))
print(ans)
