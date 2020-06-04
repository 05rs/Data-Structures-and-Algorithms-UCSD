# Uses python3
import sys

def optimal_weight(W, w):
    # dp=[[-1 for j in range(w+1)] for i in range(len(wt)+1)]
    # for i in range(len(wt)+1):
    #     for j in range(w+1):
            # if i==0 or j==0:
            #     dp[i][j]=0
            # elif wt[i-1]<=j:
            #     if wt[i-1]==j:
            #         dp[i][j]=max(wt[i-1],dp[i-1][w])
            #     else:
            #         if
            #         dp[i][j]=max(wt[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            # else:
            #     dp[i][j]=dp[i][j-1]

    c = [0] * (W+1)
    for i in range(len(w)):
        for j in range(W, w[i]-1, -1):
            c[j] = max(c[j], c[j - w[i]] + w[i])
            # print(c)
    return c[W]
# if __name__ == '__main__':
#     W, n = list(map(int, raw_input().split()))
#     w = list(map(int, raw_input().split()))
#     print(optimal_weight(W, w))
#
#     for idx in dp:
#         print(idx)
#     return dp[len(wt)][w]

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     W, n, *w = list(map(int, input.split()))
#     print(optimal_weight(W, w))
w,n=list(map(int,input().split()))
wt=list(map(int,input().split()))
print(optimal_weight(w,wt))
