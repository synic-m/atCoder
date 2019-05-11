#ろ
S = input()
K = int(input())
l = K%len(S)
print(S[l:],S[:l],sep='')
