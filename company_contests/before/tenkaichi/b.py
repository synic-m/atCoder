N = int(input())
S = input()
K = int(input())
flag = S[K-1]
ans = []
for x in S:
    if x == flag:
        ans.append(x)
    else:
        ans.append('*')
print(''.join(ans))
