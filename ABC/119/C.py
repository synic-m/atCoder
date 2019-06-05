####C-bamboo
N,A,B,C = map(int,input().split())
l =[]
for _ in range(N):
    l.append(int(input()))
INF = 10**9

def dfs(cur,a,b,c):
    if cur == N:
        if min(a,b,c) > 0:
            ans = abs(a-A) + abs(b-B) + abs(c-C) -30 
            #接合は各一回ずつ余分
        else:
            ans = INF
        return ans
    ret0 = dfs(cur+1,a+l[cur],b,       c)        + 10
    ret1 = dfs(cur+1,a,       b+l[cur],c)        + 10
    ret2 = dfs(cur+1,a,       b,       c+l[cur]) + 10
    ret3 = dfs(cur+1,a,       b,       c)        + 10
    #a,b,c,どこにも入れないの4通り
    #分けて接合 -> 10
    return min(ret0,ret1,ret2,ret3)
print(dfs(0,0,0,0))
