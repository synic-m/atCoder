#[全部作る]
s = input() 
S = [_ for _ in s]
N = len(S)-1
ans_lis = []
pra_lis = []
calis = []
for x in range(2**N):
    lis = [''] * (N)
    for y in range(N):
        if((x >> y) & 1)==1:
            lis[N-1-y] = "+"
    pra_lis.append(lis)
for z in pra_lis:
    z.append('')
    for x in range(len(S)):
        calis.append(S[x])
        calis.append(z[x])
 #   print('calis',calis)
    calis = []
    ans_lis.append(calis)
ans = 0
for l in ans_lis:
    ans_num = '0'
    for r in l:
        if r == '':
            pass
        elif r == '+':
            ans += int(ans_num)
         #   print(ans_num)
            ans_num = '0'
        else:
            ans_num += r
        #print(ans_num)
    ans += int(ans_num)
print(ans + int(s))
