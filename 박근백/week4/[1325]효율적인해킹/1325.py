import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

# solve 1 bfs

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1

    while q:
        now = q.popleft()
        cnt[start] += 1
        for el in graph[now]:
            if visited[el] == 0:
                visited[el] = 1
                q.append(el)

cnt = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    bfs(i)

max_val = max(cnt)
for i in range(1, n + 1):
    if cnt[i] == max_val:
        print(i, end = ' ')



