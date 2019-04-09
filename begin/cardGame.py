N = input()


num = list(map(int,input().split()))
num.sort(reverse = True)

print(num)
a_list = num[0::2]
print(a_list)
b_list = num[1::2]
print(b_list)
a_score = sum(a_list)
b_score = sum(b_list)
ans = a_score - b_score
print(ans)

