#c.py
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)
def lcm(a, b):
    return a * b // gcd(a,b)
a,b,c,d = map(int,input().split())
canC = int(b//c) -int((a-1)//c)
canD = int(b//d) - int((a-1)//d)
dbCD = int(b//lcm(c,d)) -int((a-1)//lcm(c,d))
print((b-a+1) -canC - canD + dbCD)
