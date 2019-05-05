from collections import deque

R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
maze = [input() for _ in range(R)]
reached = [[-1]*C for _ in range(R)]

                                    #ベクトルの設定
vx = [1,-1,0,0]
vy = [0,0,1,-1]

def bfs(y,x):
                                    #初期状態をqueに入れる
    q = deque([[y,x]])
                                    #初期到達点を0で初期化
    reached[y][x] = 0
    while q:
                                    #popする値をxyに代入する
        y,x = q.popleft()
                                    #if yx is goal
        if [y,x] == [gy-1,gx-1]:
            return reached[y][x]
                                    #ベクトルを設定していたのを使用
        for dy,dx in zip(vy,vx):
            ny,nx = y+dy,x+dx
                                    #未到達かつ迷路の道だった時
            if not (0 <= ny < R and 0 <= nx < C):
                continue
                                    #現時点到達フラグ＋１をnextフラグに入れる
                                    #最短距離が求まる
            if reached[ny][nx] == -1 and maze[ny][nx]=='.':
                reached[ny][nx] = reached[y][x] + 1 
                q.append([ny,nx])   #ベクトルの方向の先が空いているならばqueueに加える
                                    #先に加えて取り出していく

print(bfs(sy-1,sx-1))
#for x in reached:
#    print(x)
