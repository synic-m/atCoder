N,K = map(int,input().split())
ans_num = N // 2 if N%2 == 0 else N//2+1
if ans_num >= K:
    print('YES')
else:
    print('NO')
