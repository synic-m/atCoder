N = int(input())
A = list(map(int,input().split()))
a = sorted(A,reverse=True)
bef = a[0]


flag =0
ans_list = []

for x in a[2:]:
    bef %= x
print(bef)
