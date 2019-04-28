import sys
sys.setrecursionlimit(100000)
H,W = map(int,input().split())
lis = [input() for x in range(H)]
field = [x*100 for x in lis]
#print(field[0][1],'field')
reached = [[0 for x in range(W*100)]for y in range(H)]
def dr(x,y):
 #   print(x,y,'first')
    if x<0 or y<0 or x >=H or y >=100*W or field[x][y] == '#' or reached[x][y] == 1:
        return
    reached[x][y] = 1
    dr(x+1,y)
    dr(x,y+1)

dr(0,0)
if reached[H-1][W*100-1] == 1:
    print('Yay!')
else:
    print(':(')
#print(reached)
