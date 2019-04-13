S = input()
ans = 0
flag ='0'
for x in S:
    if flag != x:
        ans += 1
    if flag == '1':
        flag = '0'
    else:
        flag = '1'
print(min(ans,len(S)-ans))
