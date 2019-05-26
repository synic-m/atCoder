n,m = map(int,input().split())
lis = [list(map(int,input().split())) for x in range(m)]
key = [-1,100001]
for x in lis:
    if key[0] < x[0]:
        key[0] = x[0]
    if key[1] > x[1]:
        key[1] = x[1]
print(len(range(key[0],key[1]+1)))
