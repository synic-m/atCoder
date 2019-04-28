N = int(input())
lis = [list(map(int,input().split())) for x in range(N)]
alis = []
blis =[]
for x in lis:
    alis.append(x[0])
    blis.append(x[1])

ans_lis = [abs(a-b) for a,b in zip(alis,blis)]
ent = sorted(lis)[N//2]
#print(ent)
out = sorted(lis,key = lambda x:x[1])[N//2]
dist_enter = [abs(ent[0]-a) for a in alis]
dist_out = [abs(out[1]-b) for b in blis]
#print(ans_lis)
ans = 0
ans += sum(ans_lis)
ans += sum(dist_out)
ans += sum(dist_enter)
print(ans)
