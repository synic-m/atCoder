N = int(input())
S = input()
ans = 0
right = []
left = []
cnt = [0 for x in range(N)]
for x,y,z in zip(S[:N:],S[1::],range(N)):
    if x == '#' and y == '.':
        cnt[z] = 1
        right.append(z)
    elif x == '.' and y == '#':
        cnt[z] = -1
        left.append(z)
left.append(N-1)
try:
    if right[0]>left[0]:
        left.pop(0)
except:
    pass
for x,y in zip(right,left):
    ans += y-x
print(min(ans,N-ans))
