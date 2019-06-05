N = int(input())
ans = 0
def sft(s):
    global ans
    if int(s) >= N:
        return ans
    for x in '357':
        if int(s+x) > N:
            break
        sft(s+x)
        if '3' in s+x and '5' in s+x and '7' in s+x:
            #print(s+x)
            ans += 1
    return ans
print(sft('0'))
