n = int(input())
h_want = list(map(int,input().split()))
h_list = [0 for hoge in range(n)]
mov_lis = []
#print(n,h_want)
li_max = max(h_want)
li_min = min(h_want)
h_list = [_+li_min for _ in h_list]
ans = li_min
print(h_list,h_want)
mov_flag = 0
for _ in range(h_want.count(min(h_want))):
    mov_lis.append(h_want[mov_flag:h_want.index(min(h_want)):])
    try:
        mov_flag = h_want.index(min(h_want))
    except:
        print('pass')
        pass
print(h_want)
print(mov_lis)


