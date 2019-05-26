import sys
sys.setrecursionlimit(1000000)
N = int(input())
lis = [list(map(int,input().split())) for x in range(N-1)]+[[N,N,0]]
#[[1,2,len],[2,3],[1,3],[4,5],[5,6]]
color = [-1 for x in range(N)]
for x in range(N):
    a,b,lo=lis[x]
    if lo%2==1:
        if not (color[a-1]==1 or color[a-1]==0):
            color[a-1]=1
        if not (color[b-1]==1 or color[b-1]==0):
            color[b-1]=1
    else:
        if not (color[a-1]==1 or color[a-1]==0):
            color[a-1]=0
        if not (color[b-1]==1 or color[b-1]==0):
            color[b-1]=0
for x in color: print(x)
