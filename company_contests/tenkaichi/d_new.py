n = int(input())
s = input()
bs = 0
ws = s.count('.')
#準備すべての.を数えとく>> 現在地より右側の～カウントのため
ans = n
for c in s:
    if c == '.':
        ws -= 1
        #現在地より右側の色を変える石の数を数える. to #
    else:
        bs += 1
        #現在地より左の色を変える石の数を数える# to .
    now = ws + bs
    #変える石の数の合計
    if ans > now:
        ans = now
print(ans)
