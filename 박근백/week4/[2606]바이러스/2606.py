import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


# solve 1 disjoint_set
def find_p(x):
    if p[x] != x:
        p[x] = find_p(p[x])
    return p[x]

def union(a, b):
    ap = find_p(a)
    bp = find_p(b)
    if ap > bp:
        p[ap] = bp
    else:
        p[bp] = ap


p = [i for i in range(n + 1)]

cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n + 1):
    if find_p(i) == 1:
        cnt += 1

print(cnt - 1)



"""
#solve 2 dfs
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n + 1)]

def dfs(node):
    global cnt
    cnt += 1
    visited[node] = 1
    for ne in graph[node]:
        if visited[ne] == 0:
            dfs(ne)

cnt = 0
dfs(1)
print(cnt - 1)
"""

"""
#solve 3 bfs
from collections import deque

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    q = deque([node])
    visited = [0 for _ in range(n + 1)]
    visited[node] = 1
    count = 0
    while q:
        now = q.popleft()
        count += 1
        for ne in graph[now]:
            if visited[ne] == 0:
                visited[ne] = 1
                q.append(ne)
    return count - 1

print(bfs(1))
"""



