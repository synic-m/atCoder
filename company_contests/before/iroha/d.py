n,x,y = map(int,input().split())
lis = list(map(int,input().split()))

lis.sort()

T = sum(lis[1::2],x)
A = sum(lis[::2],y)
if T < A :
    print('Aoki')
elif A < T:
    print('Takahashi')
else:
    print('Draw')
