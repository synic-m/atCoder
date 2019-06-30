#c.py
n = int(input())
lis = list(map(int,input().split()))
lis.sort()
if lis[n//2] == lis[n//2-1]:
    print(0)
else:
    print(lis[n//2] - lis[n//2-1])
