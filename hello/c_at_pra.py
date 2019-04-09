N = int(input())
A = list(map(int,input().split()))
for main_loop in range (0,N):    
    A.sort()
    de = A.count(0)
    del A[:de]
    li = len(A)
    if A[0] == 1:
        break
    for x in range(1,li):
        A[x] = A[x]%A[0]
print(A[0])
