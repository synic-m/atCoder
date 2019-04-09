N = int(input())
L = list(map(int,input().split()))
#print (L)
L.sort()
#print(L)
A_theorem = sum(L) - L[N-1]
#print(A_theorem)
if A_theorem > L[N-1]:
    print('Yes')
else:
    print('No')

