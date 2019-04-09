S = input()
T_list = ['dream','dreamer','erase','eraser']
T = ''
for x in range(len(S)//5+1):
    S = S.replace(T_list[3],'')
    S = S.replace(T_list[2],'')
    S = S.replace(T_list[1],'')
    S = S.replace(T_list[0],'')
#print(S)
if len(S) == 0:
    print('YES')
else:
    print('NO')
