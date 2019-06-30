#d.py
n,k = map(int,input().split())
mod = 10 ** 9 + 7
def comb(N,M):
    mul = 1
    divid = 1
    for x in range(M):
        if (N-x) == 0:
            return 1
        mul *= (N-x)
        divid *= x+1
        print('mul',mul,'divid',divid)
    print('retttt',(mul//divid))
    return (mul//divid) % mod
for i in range(1,k+1):
    print(i,'--------------------------------')
    ans = comb(n-k-1,i) * (n-k-1+i)**(k-i)
              #5-3-1,123
            #red        #blue
            #oooo o
            #ooo oo
            #oo ooo
            #o oooo
    print(ans)
    print('#############################')
