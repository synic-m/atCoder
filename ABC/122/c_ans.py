N,Q = map(int,input().split())
S = input()
ansers = [0] * (N+1)
for i in range(N):
    ansers[i+1] = ansers[i] + (1 if S[i:i+2] == 'AC' else 0)
for q in range(Q):
    l,r = map(int,input().split())
    print(ansers[r-1] - ansers[l-1])

print(ansers)
