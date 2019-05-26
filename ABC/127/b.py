#b.py
r,d,x= map(int,input().split())

for N in range(10):
    x=x*r-d
    print(x)
