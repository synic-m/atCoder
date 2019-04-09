N = int(input())
T,A = map(int,input().split())
lis = list(map(int,input().split()))
tmperature = [T-_*0.006 for _ in lis]
ans_lis = [abs(A-_) for _ in tmperature]

print(ans_lis.index(min(ans_lis)) + 1)
