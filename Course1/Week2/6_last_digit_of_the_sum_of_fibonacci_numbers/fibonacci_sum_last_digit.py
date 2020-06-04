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


def fibonacci_sum_naive(n):
    # Sum of n Fibonacci numbers is F(n + 2) - 1
    sum = 0
    d=n+2
    if n+2>60:
        d=(n+2)%60
    if mem[d] != 0:
        return mem[d]-1
    else:
        return 9


memo()
n = int(input())
print(fibonacci_sum_naive(n))
