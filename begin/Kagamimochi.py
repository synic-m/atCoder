N=int(input())
d=[]
for x in range(N):
  d.append(input())
d.sort()
flag = -999
mv = 0
for _ in range(len(d)):
    if d[mv] == flag:
        d.pop(mv)
        mv -= 1
    if mv >= len(d):
        break
    flag = d[mv]
    mv += 1
print(len(d))
#print(d)
