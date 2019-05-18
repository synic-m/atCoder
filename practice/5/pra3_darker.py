h,w = map(int,input().split())
l = [input() for x in range(h)]
lis = [[x for x in S]for S in l]
ans=0
bk_lis=[]
def lis_Serch(lis):
    global bk_lis
    for x in range(h):
        for y in range(w):
            if lis[x][y] == '#':
                bk_lis.append([x,y])

def m_bfs(lis):
    global bk_lis
    ans = 0
    while True:
        for x in bk_lis:
            chc(x)
        if len(bk_lis) == h*w:
            return ans
        bk_lis=[]
        lis_Serch(lis)
        ans+=1

            
def chc(fili):
    vy = [0,0,1,-1]
    vx = [1,-1,0,0]
    for vx,vy in zip(vx,vy):
        now=[fili[0]+vy,fili[1]+vx]
        if 0<=now[0]<h and 0<=now[1]<w:
            lis[now[0]][now[1]] = '#'
lis_Serch(lis)
print(m_bfs(lis))
