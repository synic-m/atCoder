#a.py
n,m = map(int,input().split())

if n>=13:
    print(m)
elif 6<=n<=12:
    print(m//2)
else:
    print(0)
