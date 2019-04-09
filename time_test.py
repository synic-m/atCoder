import time
###################
start1 = time.time()
#####処理入力↓↓↓↓↓↓↓↓↓↓↓↓↓
ans = 0
for x in range(10**5):
    ans+=1

print(ans)
####処理入力↑↑↑↑↑↑↑↑↑↑↑↑↑
elapsed_time = time.time() - start1
print ("1_time:{0}".format(elapsed_time) + "[sec]")




