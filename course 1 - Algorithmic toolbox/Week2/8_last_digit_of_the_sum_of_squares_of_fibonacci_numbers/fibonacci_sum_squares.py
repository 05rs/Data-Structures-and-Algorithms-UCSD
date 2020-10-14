# Uses python3
import sys
mem={}
# there is a pattern in digits repeats at cycle of 60
def memo(n=60):

    mem[0]=0
    mem[1]=1
    for i in range(2,n+1):
       mem[i] = ((mem[i-1]) + (mem[i-2])%10)%10
    return



def fibonacci_sum_squares(n):

    d=n
    if n>60:
        d=n%60

    vert= mem[d]
    hor=mem[(n+1)%60]
    return (vert*hor)%10

memo()
n = int(input())
print(fibonacci_sum_squares(n))
