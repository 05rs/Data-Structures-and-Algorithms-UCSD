#Uses python3

import sys

def explore(adj,x,visited):
    for node in adj[x]:
        if not visited[node]:
            visited[node]= True
            explore(adj,node,visited)
    return
def acyclic(adj):
    result=0
    for i in range(len(adj)):
        visited=[False]*(len(adj))
        explore(adj,i,visited)
        if visited[i]:
            result=1
            break
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
