n,t = map(int,input().split())
lis = [list(map(int,input().split())) for x in range(n)]

lis = sorted(lis)
def TimeLimit(lis):
    for x in lis:
        if t >= x[1]:
            print(x[0])
            return
    else:
        print('TLE')
TimeLimit(lis)
