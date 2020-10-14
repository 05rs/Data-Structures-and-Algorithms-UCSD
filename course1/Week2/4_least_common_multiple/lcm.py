# Uses python3
import sys
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return int((a*b)/gcd(a,b))

a, b = map(int, input().split())
print(lcm(a, b))

