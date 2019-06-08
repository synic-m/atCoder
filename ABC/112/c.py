n = int(input())
lis = [list(map(int,input().split())) for x in range(n)]
lis = sorted(lis,key=lambda x:x[2])

bx,by,bh = -1,-1,-1
for cy in range(101):
    for cx in range(101):
        if bh >= 0:break
        #任意の一点を定めて基準とする
        h = abs(lis[2][0] - cx) + abs(lis[2][1] - cy) + lis[2][2]
        ok = True
        for li in lis:
            #もし高さがすべて確かに一致したときprint
            if max(h - abs(li[0]-cx) - abs(li[1]-cy),0) != li[2]:
                ok = False
                break
        if ok :
            bx,by,bh = cx,cy,h
print(bx,by,bh)
