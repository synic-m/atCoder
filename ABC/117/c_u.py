N,M = map(int,input().split())
X = list(map(int,input().split()))
if N >= M :
    print(0)
    exit()
X.sort()
flag = [b-a for a,b in zip(X,X[1:])]
flag.sort()
print(sum(flag[:M-N:]))
