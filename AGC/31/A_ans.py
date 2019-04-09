N = int(input())
S = input()
d = {}
mod = 10**9 + 7
for key in S:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
ans = 1
for x in d.values():
    ans *= x+1
print(ans % mod -1)
