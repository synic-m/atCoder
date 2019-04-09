S = input()
ans_lis = []

flag_lis = [abs(7-int(x)) for x in S[:len(S)-2]]

#print(flag_lis)
for _ in range(len(flag_lis)):
    #print('aaa',_)
    if  flag_lis[_] == min(flag_lis):
        flag = _
        ans_lis.append(int(S[flag:flag+3:]))
        #ans_lisは753からの差を表示、min(ans_lis)を表示
tp = [abs(_-753) for _ in ans_lis]
ans = min(tp)
print(ans)
#print(ans_lis)
