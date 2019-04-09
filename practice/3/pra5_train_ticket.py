S = input()
LIST = [int(_) for _ in S]
pra_fla = []
for _ in range(2**3):
    lis = ['-' for fl in range(3)]
    for x in range(3):
        if (_ >> x)&1:
            lis[x] = '+'
    pra_fla.append(lis)

ans_lis = []
for x in pra_fla:
    pre = []
    x.append('')
    for y in range(4):
        pre.append(LIST[y])
        pre.append(x[y])
    ans_lis.append(pre)
flag = 0 #0:null #1:+ #2:-
for x in ans_lis:
    ans = 0
    ans_str = ''
    for y in x:
        #print(y)
        ans_str += str(y) 
        if y == '+':
            flag = 1
        elif y == '-':
            flag = 2
        elif y == '':
            flag = 0
        else:
            if flag == 1 or flag == 0:
                ans += y
            elif flag == 2:
                ans -= y
            flag = 0
    if ans == 7:
        break
ans_str += '=7'
print(ans_str)
