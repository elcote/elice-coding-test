import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for el in graph:
    el.sort(reverse=True)

def dfs(node):
    print(node, end = ' ')
    visited[node] = 1
    for el in graph[node]:
        if visited[el] == 0:
            dfs(el)

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for el in graph[now]:
            if visited[el] == 0:
                visited[el] = 1
                q.append(el)


visited = [0 for _ in range(n + 1)]
queue = list([v])
visited[v] = 1
while queue:
    node = queue.pop()
    print(node, end=' ')
    for el in graph[node]:
        if visited[el] == 0:
            visited[el] = 1
            queue.append(el)

print()
for el in graph:
    el.sort()
visited = [0 for _ in range(n + 1)]
bfs(v)

