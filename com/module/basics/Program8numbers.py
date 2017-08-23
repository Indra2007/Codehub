#Program8numbers.py

def divide(a,b):
    q = a/b
    r = a - (q*b)
    return q,r

def gcd(x,y):
    g =y
    while x>0:
        g = x
        x = y % x
        y = g
    return g


import Program8numbers

x,y = Program8numbers.divide(42,5)
print(x,y)

n = Program8numbers.gcd(7291823, 5683)
print(n)
