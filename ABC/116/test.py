N=int(input())
h=[0]+[int(i) for i in input().split()]+[0]
s=[h[i+1]-h[i] for i in range(N+1)]
print('s',s)
print('h',h)

ans=0
for i in s:
    print('i',i)
    if i>0:
        ans+=i
        print('ans',ans)
print(ans)
