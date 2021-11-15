from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()
    
n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int,input().split())
    # graph[node1].append(node2)
    graph[node2].append(node1)
# print(graph)

cnt = [-1 for _ in range(n+1)]
maxNum = 0

def BFS(node,idx):
    global maxNum
    bfsqueue = deque()
    bfsqueue.append(node)
    while bfsqueue:
        cur = bfsqueue.popleft()
        for connectedNode in graph[cur]:
            if visited[connectedNode] == True:
                continue
            else:
                bfsqueue.append(connectedNode)
                visited[connectedNode] = True
                cnt[idx] += 1
                if maxNum < cnt[idx]:
                    maxNum = cnt[idx]


for i in range(1,n+1):
    visited[i] = True
    BFS(i,i)
    for i in range(1,n+1):
        visited[i] = False

for i in range(1,n+1):
    if maxNum == cnt[i]:
        print(i,end=' ')