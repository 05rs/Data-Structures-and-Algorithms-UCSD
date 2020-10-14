# Uses python3
import sys

def optimal_sequence(num):
    temp=[num+1]*(num+1)
    temp[0]=0
    temp[1]=0
    if num>=2:
        for i in range(2,num+1):
            if i/3==i//3 and i/2==i//2:
                temp[i]=min(temp[i//2],temp[i//3],temp[i-1])+1
            elif i/3==i//3 and not i/2==i//2:
                temp[i]=min(temp[i//3],temp[i-1])+1
            elif i/2==i//2 and not i/3==i//3:
                temp[i]=min(temp[i//2],temp[i-1])+1
            else:
                temp[i]=temp[i-1]+1
    items=list()
    items.append(num)
    n=num
    while n>1:
        if n/3==n//3 and temp[n//3]==temp[n]-1:
            items.append(n//3)
            n=n//3
        elif n/2==n//2 and temp[n//2]==temp[n]-1:
            items.append(n//2)
            n=n//2
        else:
            items.append(n-1)
            n=n-1
    return items

input = sys.stdin.read()
n = int(input)
sequence=optimal_sequence(n)
print(len(sequence) - 1)
print(*reversed(sequence))

