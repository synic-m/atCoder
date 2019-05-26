n,k=map(int,input().split())
p_lis = []
for x in range(1,n+1):
    if k>x:
        i=1
        while x*2<k:
            x*=2
            i+=1
        p_lis.append(((1/2)**i)*(1/n))
    else:
        p_lis.append(1/n)
print(sum(p_lis))
