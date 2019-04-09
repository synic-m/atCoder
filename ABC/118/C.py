N = int(input())
A = list(map(int,input().split()))
while len(A) > 1:
    a_ = A[0]
    for x in range(1,len(A)):
        A[x] %= a_
    A = [ans for ans in A if ans > 0]
    A.sort()
print(A[0])

