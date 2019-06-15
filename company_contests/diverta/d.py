n=int(input())
li=[]
ans=0
for x in range(1,int(n**0.5)+1):
    if n%x == 0:
        li.append(x)
        if x != n//x:
            li.append(n//x)
li.pop(0)
for x in li:
    if n//(x-1) == n%(x-1):
        ans+=x-1
print(ans)
