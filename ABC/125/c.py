def gcd(a,b):
    if (b==0):
        return a
    return gcd(b,a%b)


n = int(input())
a = list(map(int,input().split()))
l = [0 for x in range(n+1)]
r = [0 for x in range(n+1)]
#l left ->左から n番目までの最大公約数
#r right -> 右からn番目までの最大公約数
#l#L(i) = A1,A2,A3...A(i-1) の最大公約数
#r#R(i) = Ai,A(i+1),....AN の最大公約数
#gcd(L(i),R(i)) はA{1..N}の最大公約数と同義
#max -> 1 個消す動作と等しい
#-->>  ans のリストは（ここではans）gcd(L(i),R(i+1))
#                                              ~~~
#(A1,A2,A3,...A(i-1),A(i+1)...AN) <- ↑の内容
#これでiを除くgcdになる
for x in range(n):
    l[x+1] = gcd(l[x],a[x])
    r[n-x-1] = gcd(r[n-x],a[n-x-1])

##
#
#print(a)
#print(l,r)
ans = 0
for x in range(n):
    #print(ans,l[x],r[x+1],gcd(l[x],r[x+1]))
    ans = max(ans,gcd(l[x],r[x+1]))
#
print(ans)
