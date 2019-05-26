n,m = map(int,input().split())
alis = list(map(int,input().split()))
lis = [list(map(int,input().split())) for x in range(m)]
for x in alis:
    lis.append([1,x])
lis.sort(reverse=True,key=lambda x:x[1])
ans = 0
for x in lis:
    (number,point) = x
    if number >= n:
        number = n
        ans += number * point
        #print(n)
        #print(ans,'+=',number,'*',point)
        break
    ans += number * point
    n -= number
    #print(n)
    #print(ans,'+=',number,'*',point)
print(ans)
#print(lis)
