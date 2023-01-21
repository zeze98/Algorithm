import math

def lcm(a,b):
    return (a*b) // math.gcd(a,b)

x, y = map(int,input().split())
print(math.gcd(x,y))
print(lcm(x,y))