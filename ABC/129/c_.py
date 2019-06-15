import sys
mod = 10 ** 9 + 7

n,m = map(int,input().split())
if n in [0,1]:
    print(1)
    sys.exit()
    
if not m == 0: lis = [int(input()) for x in range(m)]
else: lis = [-1]
val1 = 1
if 1 in lis: val2 = 0
else: val2 = 1

if lis[0] == 1 and len(lis) >= 2:
    flg = lis[1]
    nex = 1
else:
    flg = lis[0]
    nex = 0
#print(lis)
for x in range(2,n):
    if x == flg: #x in lis
        #print(flg)
        nex += 1
        try: flg = lis[nex]
        except:flg = 0
        now = 0
    else:
        now = (val1 + val2) % mod
    val1,val2 = val2,now
    
print((val1 + val2) % mod)
    
