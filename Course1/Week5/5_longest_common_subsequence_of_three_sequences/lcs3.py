#Uses python3

import sys

def lcs3(a, b,c):
    count=0
    m_c=0
    m=len(a)
    n=len(b)
    k=len(c)
    dp = [[ [-1 for i in range(k+1)] for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            for k in range(k+1):
                # print(i,j)
                if i==0 or j==0 or k==0:
                    dp[i][j][k]=0
                elif a[i-1]==b[j-1]==c[k-1]:
                    dp[i][j][k]=1 + dp[i-1][j-1][k-1]
                else:
                    dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])

    return dp[m][n][k]


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#
#     n = data[0]
#     data = data[1:]
#     a = data[:n]
#
#     data = data[n:]
#     m = data[0]
#     data = data[1:]
#     b = data[:m]
m=int(input())
a=list(input().split())
n=int(input())
b=list(input().split())
k=int(input())
c=list(input().split())
print(lcs3(a, b,c))

