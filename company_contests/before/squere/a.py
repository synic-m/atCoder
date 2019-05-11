N,T = map(int,input().split())
lis = list(map(int,input().split()))
time = sum(lis)
if time % T == 0:
    ans = time//T 
else:
    ans = time//T+1
print(ans)
