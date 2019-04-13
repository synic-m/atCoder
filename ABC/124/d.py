#looked ans

n,k = map(int,input().split())
s = input()
#入力
cnt = 0
if s[0] == '0':
    cnt += 1
for i in range(1,n):
    if s[i-1] == '1' and s[i] == '0':
        cnt += 1
##切り替わるところで＋1
if cnt <= k:
    print(n)
    #切り替わるところが動かす回数より少ない場合n(自明)
else:
    one_left,one_right = [0],[]
    #
    for i in range(1,n):
        if s[i-1] == '0' and s[i] == '1':
            one_left.append(i)
        if s[i-1] == '1' and s[i] == '0':
            one_right.append(i)
    #01 の時右に加える10の時左に加える
    #切り替えの時の配列の番号を加える
    one_right.append(n)
    #nはとりあえず右
    if s[0] == '1':
        one_right.pop(0)
    if s[-1] == '1':
        one_left.pop(-1)
    #最初の人が逆立ちしているなら右の切り替えの最初はなし
    #最後の人が逆立ちしているなら左の切り替えの最後はなし
    #print(one_right,'r')
    #print(one_left,'l')

    ans = 0
    #ans 01,10の切り替えの少ないほうでloopを回す
    for i in range(min(len(one_left),len(one_right)-k+1)):
        ans = max(ans,one_right[i+k-1]-one_left[i])
        #ans は　ある点までの個数-フラグの開始点までの個数の最大値
    print(ans)

