# Uses python3
import sys

def get_majority_element(a):
    count= {}
    for it in a:
        if it not in count:
            count[it]=0
        elif count[it]>=(len(a)//2):
            return 1
        else:
            count[it]+=1
            if count[it]>=(len(a)//2):
                return 1
    return 0


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *a = list(map(int, input.split()))
#     if get_majority_element(a, 0, n) != -1:
#         print(1)
#     else:
#         print(0)
n=int(input())
a = list(map(int, input().split()))
# print(n,a)
print(get_majority_element(a))
# if get_majority_element(a,n) != -1:
#     print(1)
# else:
#     print(0)
