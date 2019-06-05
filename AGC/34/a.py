n,a,b,c,d = map(int,input().split())
s = input()
flg = False
if c < d:
    #最後まで動かす
    flg = True
else:#c>d
    if '...' in s[b-2:d+1]:
        flg = True
if '##' in s[a-1:max(d,c)-1]:
    flg = False
if flg:
    print('Yes')
else:
    print('No')
