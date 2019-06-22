#b.py
n,l = map(int,input().split())
if l < 0 and n > abs(l):
    print(int((n+2*l-1)*n/2))
else:
    if l < 0:
        print(int((n+2*l-1)*n/2 -l-n+1))
    else:
        print(int((n+2*l-1)*n/2 -l))
