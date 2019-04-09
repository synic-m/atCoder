N,M = list(map(int,input().split()))
A = []
B = []
ans = 0
for _ in range(N):
    i = list(map(int,input().split()))
    A.append(i[0])
    B.append(i[1])
while M != 0:
    ind_ = A.index(min(A))
    if M - B[ind_] > 0:
        M -= B[ind_]
        ans += A[ind_]*B[ind_]
        B[ind_] -= B[ind_]
    else:
        ans += A[ind_]*M
        break
    if B[ind_] <= 0:
        B.pop(ind_)
        A.pop(ind_)
print(ans)
