#c.py
from math import gcd
def lcm(a, b):
    return a * b // gcd(a,b)
a,b,c,d = map(int,input().split())
canC = b//c -(a-1)//c
canD = b//d - (a-1)//d
dbCD = b//lcm(c,d) -(a-1)//lcm(c,d)
print((b-a+1) -canC - canD + dbCD)
