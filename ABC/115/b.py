N = int(input())
lis = [int(input()) for x in range(N)]
lis[lis.index(max(lis))] = max(lis)//2
print(sum(lis))
