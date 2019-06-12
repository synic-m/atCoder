n = input()
ans = ''
for s in n:
    if s == '9':
        ans += '1'
    else:
        ans += '9'
print(ans)
