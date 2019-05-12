n=int(input())
ans=0
flagA=[]
flagB=[]
fla=0
flb=0
for x in range(n):
    s = input()
    if 'AB' in s:
        ans += s.count('AB')
    if s[-1]=='A':
        flagA.append(x)
        fla+=1
    if s[0]=='B':
        flagB.append(x)
        flb+=1
if flagA==flagB and len(flagA)!=0:
    ans-=1
ans+=min(fla,flb)
print(ans)
