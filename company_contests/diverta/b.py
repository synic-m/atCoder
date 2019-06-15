R,G,B,n=map(int,input().split())
ans=0
for r in range(((n+1)//R)+1):
    for g in range(((n+1)//G)+1):
        if ((n-r*R - g*G)%B)== 0 and (n-r*R-g*G)>=0:
            ans+=1
print(ans)
