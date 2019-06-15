#a.py 100
n,k = map(int,input().split())
if k ==1 or k == n:
    print(0)
else:
    print(n-k)
