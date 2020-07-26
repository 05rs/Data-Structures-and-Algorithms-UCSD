#Uses python3
def reach(adj):
    #write your code here
    visited = [0] * len(adj)
    rank=0
    for i in range(len(adj)):
        if visited[i]==0:
            rank+=1
            explore(adj,i,visited,rank)
    return max(visited)


def explore(adj,x,visited,rank):
    if (visited[x] == rank):
        return
    visited[x] = rank
    for i in range(len(adj[x])):
      if (not visited[adj[x][i]]):
          if(explore(adj,adj[x][i],visited,rank)):
              return
    return 0



data = list(map(int, input().split()))
n, m = data
adj = [[] for _ in range(n)]
for _ in range(m):
    a,b=list(map(int, input().split()))
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
print(reach(adj))
