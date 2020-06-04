import math

class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def dis (p1,p2):
    return math.sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y))

def brute_force(P,n):

    min_val=float('inf')
    for i in range(n):
        for j in range(i+1,n):
            if dis(P[i],P[j]) < min_val:
                min_val=dis(P[i],P[j])
    return min_val


def close_pair(p,n):
    # if n<=3:
    #     return brute_force(p)
    if n<=3:
        return brute_force(p,n)
    mid=n//2
    ld=close_pair(p[:mid],mid)
    rd=close_pair(p[mid:],n-mid)
    d=min(ld,rd)
    # creating strip
    # midl = (p[mid].x + p[mid+1].x)/2
    midl=p[mid].x
    s1 = [i for i in p if abs(midl-i.x)<d]
    if len(s1)==0:
        return d
    s1.sort(key = lambda point:point.y)
    for i in range(len(s1)-1):
        j = 0
        while i+j+1<len(s1)  :
            if(j>5): break
            j+=1
            d = min(d,dis(s1[i],s1[i+j]) )
    return d



# INPUT
n=int(input())
p=[0]*n
for idx in range(n):
    dat=list(map(int,input().split()))
    p[idx]=point(dat[0],dat[1])

# # TO Print
# for idx in p:
#     print(idx.x,idx.y)
y_so=p.sort(key=lambda point:point.y)
# print(brute_force(p)) # brute force approach
p.sort(key=lambda point:point.x)
print("{0:.9f}".format(close_pair(p,n)))
# print(brute_force(p,n))
# print(close_pair(p,n))
