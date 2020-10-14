# Uses python3
import sys
# 1 3 4
def get_change(money,temp,dom):
    temp[0]=0
    for m in range(1,(money+1)):

        for coin in dom:
            if m>=coin:
                ncoins= temp[m-coin]+1
                temp[m]=min(temp[m],ncoins)
    return temp[money]


if __name__ == '__main__':
     m = int(sys.stdin.read())
     temp=[m+1]*(m+1)
     dom=[1,3,4]
     print(get_change(m,temp,dom))

