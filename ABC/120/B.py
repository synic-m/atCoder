A,B,K = map(int,input().split())
ans_list = []
for _ in range(1,101):
    if A % _ == 0 and B % _ == 0:
        ans_list.append(_)
#print(ans_list)
#print(len(ans_list)-K)
print(ans_list[len(ans_list)-K])
