A,B,C,X = [int(input()) for _ in range(4)]
ans = 0
for x in range(A+1):
    for y in range(B+1):
        for z in range(C+1):
            if x*500 + y*100 + z*50 == X:
                ans += 1
print(ans)
