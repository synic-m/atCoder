X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
lis = []
A.sort(reverse = True)
B.sort(reverse = True)
C.sort(reverse = True)
abc = [A,B,C]
count = 0
while True:#abc[0]
    abc.sort(reverse=True)
    print(abc)
    ele = abc[0][count]
    count_b = 0
    while True:#abc[1]
        ele += abc[1][count_b]
        count_c = 0
        while True:#abc[2]
            print(ele + abc[2][count_c])    
            
            count_c += 1
            if count_c >= len(C):
                break
        ele -= abc[1][count_b]
        count_b += 1
        if count_b == len(B):
            break

    lis.append(hoge)
    count += 1
    if count == K:
        break

print("end")
