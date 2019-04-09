### contest中にできたTLEのやつ
def is_unq(seq):
    return len(seq) == len(set(seq))

n = int(input())
S = input()
Sli = list(S)
ans_s = [[] for _ in range(1,n+1)]
ans = 0
for x in range(n):
    lis = list(cmb(Sli,x+1))
    ans_s[x] += lis
    for y in range(len(ans_s[x])):
        if is_unq(ans_s[x][y]) == True:
            ans += 1
print(ans)
