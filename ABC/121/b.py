N,M,C = map(int,input().split())
B = list(map(int,input().split()))
ans = 0
for _a in range(N):
    flag = C
    A = list(map(int,input().split()))
    for _ans in range(M):
        flag = flag + A[_ans]*B[_ans]
    if flag > 0:
        ans += 1
print(ans)
