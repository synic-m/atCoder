lis = [int(input()) for _ in range(5)]
ans_fla_lis = []

for x in lis:
    if x%10 == 0:
        ans_fla_lis.append(0)
    else:
        ans_fla_lis.append(10-(x%10))
axo = ans_fla_lis.pop(ans_fla_lis.index(max(ans_fla_lis)))
print(sum(lis) + sum(ans_fla_lis))

