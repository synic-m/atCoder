N = int(input())
A = list(map(int,input().split()))
while len(A) > 1:
    A.sort()
    devided_num = int(A[0])
    devi_lis = [devided_num]
    As = A
    As.pop(0)
    A =[_%devided_num for _ in As if _%devided_num > 0]
    A += devi_lis
print(A[0])
