import time
########first_input
S = input()
###################
start = time.time()
#####処理入力↓↓↓↓↓↓↓↓↓↓↓↓↓
T_list = ['dream','dreamer','erase','eraser']
S = S.replace(T_list[3],'').replace(T_list[2],'').replace(T_list[1],'').replace(T_list[0],'')
if len(S) == 0:
    print('YES')
else:
    print('NO')
#####処理入力↑↑↑↑↑↑↑↑↑↑↑↑↑
elapsed_time = time.time() - start
print ("1_time:{0}".format(elapsed_time) + "[sec]")
