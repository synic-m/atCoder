S = input()
ans = 0
ans_lis = [0]
for x in S:
    if x == 'A' or x == 'C' or x == 'G' or x == 'T':
        ans += 1
    else:
        ans_lis.append(ans)
        ans = 0
ans_lis.append(ans)
print(max(ans_lis))

