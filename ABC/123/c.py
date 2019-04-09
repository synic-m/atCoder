##無理解でしたorz
##できると思ったのに。。。:D
N = int(input())
lis = [int(input()) for _ in range(5)]
ans_lis=[]
now = [N,0,0,0,0,0]
ans = 0
for x in range(5):
    print(now)
    if now[x] <= lis[x]:
        where = 1
    else:
        if now[x]%lis[x] == 0:
            where = N//lis[x]
            print('if where',where)
        else:
            where = N//lis[x]+1
        print('a',where)
        ans+=where+1
    now[x] = 0
    need = []
    for _ in range(5):
        print(lis[4-_])
        now_ele = ans*(lis[4-_])-sum(need)
        need.append(now_ele)
    now =[0] + need[::-1]
print(ans)
