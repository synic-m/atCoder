N,M = map(int,input().split())
X = list(map(int,input().split()))
if N > M :
    print(0)

else:
    flag = [0 for fl in range(M)]
    X.sort()
    #print(X)
    for _ in range(1,M+1):
        flag[_] += X[_] - X[_-1]

    print(flag)
    for lp in range(len(flag)):
        flag.pop(flag.index(max(flag)))
        print(sum(flag))
