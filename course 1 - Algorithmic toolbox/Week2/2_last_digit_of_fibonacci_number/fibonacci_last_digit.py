# Uses python3
mem={}
# there is a pattern in digits repeats at cycle of 60
def memo(n=60):

    mem[0]=0
    mem[1]=1
    for i in range(2,n+1):
       mem[i] = ((mem[i-1]) + (mem[i-2])%10)%10
    return
def get_fibonacci_last_digit_naive(num):
    d=num%60
    print(mem[d])
    return
memo()
n = int(input())
get_fibonacci_last_digit_naive(n)
# import random
# while True:
#     num=random.randrange(10**5,10**6)
#     print(num)
#     get_fibonacci_last_digit_naive(num)
#


