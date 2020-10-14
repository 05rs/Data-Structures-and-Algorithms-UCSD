# Uses python3
import sys

def get_change(m):
    t=0
    f=0
    o=0
    t=int(m/10)
    if int(m%10) >= 5:
        f=int(int(m%10)/5)
        o=(int(m%10)-5*f)
    else:
        o=int(m%10)
    # print(t,f,o)
    return t+f+o

m = int(input())
print(get_change(m))
