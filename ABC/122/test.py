N,Q = map(int,input().split())
S = input()
lr = [list(map(int,input().split())) for _ in range(Q)] + [0]
for q in range(Q):
    ans = 0
    for a,b in zip(S[lr[q][0]:lr[q][1]],S[lr[q+1][0]:lr[q+1][1]]):
        if a == 'A' and b == 'C':
            ans += 1
    print(ans)
