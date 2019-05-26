n,m = map(int,input().split())
xyz = [list(map(int,input().split())) for x in range(m)]

checked = [x for x in range(1,n+1)] #checked = 0
xyz.sort()
ans=n
for i in xyz:
    x,y,z = i
    if x in checked and y in checked:
        checked[x-1]=0
        checked[y-1]=0
        ans-=1 #no check
    elif x in checked or y in checked:
        checked[x-1]=0
        checked[y-1]=0
        ans-=1 #one check
    else:
        pass
print(ans)
