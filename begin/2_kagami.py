N = int(input())
lis = []
for x in range(N):
    a = input()
    if a not in lis:
        lis.append(a)
print(len(lis))
