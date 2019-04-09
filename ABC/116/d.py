N,K =map(int,input().split())
td = [list(map(int,input().split())) for x in range(N)]
norm = 0
t = [td[_][0] for _ in range(N)]
d = [td[_][1] for _ in range(N)]
dt = list(zip(d,t))
scope = max(td)[0] - min(td)[0] +1
ch_flag = scope **2
dt.sort(reverse = True)
d.sort(reverse = True)
print(dt)
for y in range(K):
    norm += d[y]
print(norm)
