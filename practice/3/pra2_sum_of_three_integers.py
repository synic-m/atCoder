K,S = map(int,input().split())
ans = 0
for a in range(K+1):
    for b in range(K+1):
        c = S - a - b
        if 0 <= c and c <= K:
            ans += 1
print(ans)
