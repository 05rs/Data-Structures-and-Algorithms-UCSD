 # Uses python3
import sys
import random

# def partition3(a, l, r):
#     #write your code here
#     p=a[l]
#     i=j=l
#     for idx in range(l+1,r+1):
#         if a[idx]<p:
#             i+=1
#             a[idx],a[i]=a[i],a[idx]
#         if a[idx]==p:
#             if j<i:
#                 j=i+1
#             else:
#                 j+=1
#             a[idx],a[j]=a[j],a[idx]
#     a[l],a[i]=a[i],a[l]
#     return i,j
def partition3(a, l, r):
    #write your code here
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
    	if a[i] < x:
        	a[i],a[m1] = a[m1],a[i]
        	m1+=1
        	m2+=1
        	a[i],a[m2] = a[m2],a[i]
    	elif a[i] == x:
        	m2+=1
        	a[i],a[m2] = a[m2],a[i]
   # a[l],a[m1] = a[m1],a[l]
    return m1,m2

    pass

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    i,j = partition3(a, l, r)
    randomized_quick_sort(a, l, i - 1);
    randomized_quick_sort(a, j + 1, r);



# input = sys.stdin.read()
n=int(input())
a = list(map(int, input().split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
