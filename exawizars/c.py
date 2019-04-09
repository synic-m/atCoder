##TLE 知ってた
N,Q = map(int,input().split())
S = input()
ans_lis = [1 for x in S]
spell = [list(input().split()) for _ in range(Q)]


for x in spell:
    mv = x[0]
    mv_v = x[1]
    if mv_v == 'R':
        vect = 1
        if mv == S[N-1]:
            ans_lis[N-1] = 0
        for y in reversed(range(N-1)):
            if S[y] == mv:
                ans_lis[y+1] += ans_lis[y]
                ans_lis[y] = 0
    else :
        vect = -1
        if mv == S[0]:
            ans_lis[0] = 0
        for y in range(1,N):
            if S[y] == mv:
                ans_lis[y-1] += ans_lis[y]
                ans_lis[y] = 0
 
print(sum(ans_lis))
