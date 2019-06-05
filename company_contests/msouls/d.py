n = int(input())
lis = [list(map(int,input().split())) for x in range(n-1)]
clis = list(map(int,input().split()))
ans_lis = [0]*n
ans = 0
for x in lis:
    ans += min(clis[x[0]-1],clis[x[1]-1])
    ans_lis[x[0]-1] = clis[x[0]-1]
    ans_lis[x[1]-1] = clis[x[1]-1]
print(ans)
print(*ans_lis)
