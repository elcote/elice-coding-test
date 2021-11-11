import sys
def input():
    return sys.stdin.readline().rstrip()
    
n = int(input())
pairs = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(pairs):
    node1, node2 = map(int,input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

cnt = 0

def DFS(node):
    global cnt
    if visited[node] == True:
        return
    else:
        visited[node] = True
        cnt += 1
        for v in graph[node]:
            DFS(v)
            
DFS(1)
print(cnt-1)