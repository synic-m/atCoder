K,A,B = list(map(int,input().split()))
yen = 0
if B < A:
    print(K+1)#,0)
elif B+1 < K-2:
    print(K+1)#,1)
else:
    print(((K-(2* (K//A) ))//A)*B+1,'___!')

