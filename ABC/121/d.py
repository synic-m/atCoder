def calcF(n):
    if n%2 == 0:
        if n%4 == 0:
            return n
        else:
            return n^1
    else:
        if (n+1)%4 == 0:
            return 0
        else:
            return 1
A,B = map(int,input().split())
ans_A = calcF(A-1)
#print(ans_A)
ans_B = calcF(B)
#print(ans_B)
ans = ans_A^ans_B
print(ans)
