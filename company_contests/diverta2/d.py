n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if A[0] / B[0] >= A[1]/B[1] and A[0] / B[0] >= A[2] / B[2]:
    idx = 0
    if A[1]/B[1] > A[2]/B[2]:
        idx2 = 1
        midx = 2
    else:
        idx2 = 2
        midx = 1
elif A[1] / B[1] >= A[0]/B[0] and A[1] / B[1] >= A[2] / B[2]:
    idx = 1
    if A[0]/B[0] > A[2]/B[2]:
        idx2 = 0
        midx = 2
    else:
        idx2 = 2
        midx = 0

elif A[2] / B[2] > A[0]/B[0] and A[2] / B[2] > A[1] / B[1]:
    idx = 2
    if A[1]/B[1] > A[0]/B[0]:
        idx2 = 1
        midx = 0
    else:
        idx2 = 0
        midx = 1
else:
    print(aaa)
#A -> B
ans = n
money = n // A[idx]
ans1 = money * B[idx]
if n%A[idx] != 0:
    dn = n % A[idx] 
    #残りのドングリ
    money = dn // A[idx2]
    ans1 += money * B[idx2]
    if dn % A[idx] != 0:
        dng = dn % A[idx2]
        money = dng // A[midx]
        ans1 += money * B[midx]
#B -> A
money = n // B[midx]
ans2 = money * A[midx]
if n%B[idx] != 0:
    dn = n % B[midx]
    money = n // B[idx2]
    ans2 += money * A[idx2]
    if dn % B[idx] != 0:
        dng = dn % B[idx2]
        money = dng // B[idx]
        ans2 += money * A[idx]
print(max(ans,ans1,ans2))



