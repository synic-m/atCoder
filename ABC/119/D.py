A,B,Q = map(int,input().split())
abl = []
ql = []
for _a in range(A+B):
    abl.append(int(input()))
for _q in range(Q):
    ql.append(int(input())) 
mini = 0
for _ in range(Q):
    q = ql[_]
    ans_serch = list(map(abs,map(lambda lam:q - lam,abl)))
    ans_num = ans_serch.index(min(ans_serch)) 
    ans__ = abl[ans_num]
    ans_ = min(ans_serch)
    if ans_num< A:
        ans_serch = abl[A:]
        print(ans_ + abs(min(ans_serch)-ans__))#,'tomatoma')
    elif ans_num>= A:
        ans_serch = abl[0:A]
        #print(ans_,ans__,'ans_,ans__')
        #print(ans_serch,'ans_serch')
        ans = min(list(map(abs,map(lambda mi:mi - ans__,ans_serch))))
            ans += ans_
        print(ans)#,"aaaaaa")
