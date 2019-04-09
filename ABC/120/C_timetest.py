import time
########first_input

S = input()
###################
start = time.time()
#####処理入力↓↓↓↓↓↓↓↓↓↓↓↓↓

N = len(S)
for _ in range(N//2):
    S = S.replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','').replace('01','').replace('10','')

    if S.count('01') == 0 and S.count('10') == 0:
        break
print(N - len(S))


####処理入力↑↑↑↑↑↑↑↑↑↑↑↑↑
elapsed_time = time.time() - start
print ("1_time:{0}".format(elapsed_time) + "[sec]")

