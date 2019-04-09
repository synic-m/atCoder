N,M = map(int,input().split())
K = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#人ループ
for person in range(0,N):
    L = list(map(int,input().split()))
    for kind in range(1,L[0]+1):
        K[L[kind]] += 1
print(K.count(N))
