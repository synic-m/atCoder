s = int(input())
ans = -999
ans_list = []
counter = 1
ans_list.append(s)
while   True:
    counter += 1
    if s%2 == 0:
        s = s//2
    else:
        s = 3*s +1

    if  s in ans_list:
        ans = counter
        break
    elif  counter > 1000000:
        break
    ans_list.append(s)
#print('a = ',ans_list)
print(ans)
