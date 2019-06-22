n,m,x,y = map(int,input().split())
xlis = list(map(int,input().split()))
ylis = list(map(int,input().split()))
xlis.sort()
ylis.sort()
if xlis[-1] < ylis[0] and x < ylis[0] < y:
    print('No War')
else:
    print('War')
