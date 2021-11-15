import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
x, answer, answer_list = 0, 0, []

queue = deque()

visited = [False] * (n+1)

def bfs(v):
  queue = deque()
  queue.append(v)
  visited = [False] * (n+1)
  visited[v] = True
  cnt = 1

  while queue:
    target = queue.popleft()
    
    for new_target in graph[target]:
      if not visited[new_target]:
        queue.append(new_target)
        visited[new_target] = True
        cnt += 1
  return cnt

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

for i in range(1, len(graph)):
  if len(graph[i]) > 0:
    x = bfs(i)ç
    if answer < x:
      answer = x
      answer_list = [i]
    elif answer == x:
      answer_list.append(i)

for ans in answer_list:
  print(ans, end='')

print()


