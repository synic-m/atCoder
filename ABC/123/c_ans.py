N = int(input())
lis = [int(input()) for x in range(5)]
mi = min(lis)
if N%mi == 0:
    mini = N//mi
else:
    mini = N//mi +1
print(mini + 4)
