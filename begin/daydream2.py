S = input()
T_list = ['dream','dreamer','erase','eraser']
S = S.replace(T_list[3],'').replace(T_list[2],'').replace(T_list[1],'').replace(T_list[0],'')
if len(S) == 0:
    print('YES')
else:
    print('NO')
