D,G = map(int,input().split())

p_lis = [list(map(int,input().split())) for x in range(D)]
# 問題数だけ全探索
#完全に解いた時の配点
score_lis = []
for x in range(1,D+1):
    bscore = p_lis[x-1][0]*x*100 + p_lis[x-1][1]
    score_lis.append(bscore)
print(score_lis)

for x in range(2**d):
    for y in range(d):
        if (x>>y)&1:
            #flag = 1




print(D,G,p_lis)
