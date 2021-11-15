import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
    
N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
DFSvisited = [False for _ in range(N+1)]
BFSvisited = [False for _ in range(N+1)]
dfs = []
bfs = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for subGraph in graph:
    subGraph.sort()
# print(graph)
def DFS(node):
    if DFSvisited[node] == True:
        return
    else:
        DFSvisited[node] = True
        dfs.append(node)
        for v in graph[node]:
            DFS(v)

def BFS(node):
    bfsqueue = deque()
    bfsqueue.append(node)
    while bfsqueue:
        cur = bfsqueue.popleft()
        bfs.append(cur)
        for connectedNode in graph[cur]:
            if BFSvisited[connectedNode] == True:
                continue
            else:
                bfsqueue.append(connectedNode)
                BFSvisited[connectedNode] = True


DFS(V)
print(*dfs)
# print(graph)
BFSvisited[V] = True
BFS(V)
print(*bfs)