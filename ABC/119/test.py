import bisect
A,B,Q = map(int,input().split())

INF = 10**18
s= [-INF] + [int(input()) for i in range(A+B)] + [INF]
s.sort()
for q in range(Q):
    x = int(input())

print(s)
input()
input()
