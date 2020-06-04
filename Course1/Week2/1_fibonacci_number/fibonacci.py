# Uses python3

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

n=int(input())
print(calc_fib(n))

