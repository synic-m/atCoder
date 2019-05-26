#b.py
n = int(input())
lis = [list(input().split())+[x] for x in range(n)]
lis = sorted(lis,key=lambda x:x[0])
now = lis[0][0]
ans_lis = []
sublis = []
for x in lis:
    if x[0] == now:
        sublis.append(x)
    else:
        now = x[0]
        sublis = sorted(sublis,key=lambda x:int(x[1]),reverse=True)
        ans_lis.append(sublis)
        sublis = []
        sublis.append(x)
sublis.sort(key=lambda x:int(x[1]),reverse=True)
ans_lis.append(sublis)
sublis = []
sublis.append(x)       
ans_lis = [item for sublist in ans_lis for item in sublist]
for x in ans_lis:
    print(x[2]+1)

