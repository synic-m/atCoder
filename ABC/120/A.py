A,B,C = map(int,input().split())
if A*C <= B:
    print(C)
elif A*C > B:
    print(B//A)
