# Uses python3
def edit_distance(a,b):
    m=len(a)
    n=len(b)
    dp = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            # print(i,j)
            if i==0 or j==0:
                if i==0 and j==0:
                    dp[i][j]=0
                    # print('hell',dp)
                elif i==0:
                    dp[i][j]=dp[i][j-1] + 1
                else:
                    dp[i][j]=dp[i-1][j] + 1

            elif a[i-1]!=b[j-1]:
                dp[i][j]= min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
            elif a[i-1]==b[j-1]:
                dp[i][j]=dp[i-1][j-1]

            # print(dp)
    return dp[m][n]

a=input()
b=input()
print(edit_distance(a,b))

