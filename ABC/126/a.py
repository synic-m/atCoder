N,K=map(int,input().split())
s=input()
S=s.lower()
print(s[:K-1]+S[K-1:K]+s[K:])
