n = int(input())
h = list(map(int,input().split()))
ans,pre = 0,0
print(h)
for i in h:
    print('i',i)
    if pre < i:
        ans += i-pre
        print('ans += i-pre',i-pre)
        print('ans',ans)
        print('pre',pre)
    pre = i
 
print(ans)
