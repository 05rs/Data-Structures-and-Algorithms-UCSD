# Uses python3
import sys
mem={}
def calc_fib(n):
    if n in mem:
        return mem[n]
    elif n == 0:
                num = 0
    elif n == 1:
                num = 1
    elif n == 2:
        num = 1
    else:
        num=calc_fib(n - 1) + calc_fib(n - 2)
    mem[n]=num
    return num
memo={}
temp=0
def get_pisano(m):
    memo[0]=0
    memo[1]=1
    i=1
    while True:
        i=i+1
        memo[i]=calc_fib(i)%m
        if memo[i-1]==1 and memo[i-2]==0:
            temp=i-2
            if temp>1:
                return temp
def get_fibonacci_huge_naive(n, m):
    return memo[n%get_pisano(m)]

n, m = map(int, input().split())
print(get_fibonacci_huge_naive(n, m))
