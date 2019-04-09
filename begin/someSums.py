n,a,b = map(int,input().split())

#print(n)
li = [x+1 for x in range(n)]
list_ = [x+1 for x in range(n)]
#print(li)
ans = 0
for _ in range(n):
    flag = 0
    while True:
        flag += list_[_] % 10
        list_[_] = list_[_]//10
        if list_[_] == 0:
            break
    #print('flamigo',flag)
    if a>=flag or flag>=b:
        pass
    ans += li[_]
print(ans)
