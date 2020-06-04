# python3


def max_pairwise_product(numbers):
    a=max(numbers)
    numbers.remove(a)
    b=max(numbers)
    return a*b
input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))
