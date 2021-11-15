import sys

def input():
  return sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
  line = list(map(int, input().split()))
  matrix[line[0]][line[1]] = 1
  matrix[line[1]][line[0]] = 1


def bfs(node):
  visited = [node]
  queue = [node]
  while queue:
    n = queue.pop(0)
    for c in range(len(matrix[node])):
      if matrix[n][c] == 1 and (c not in visited):
        visited.append(c)
        queue.append(c)
  return visited

def dfs(node, visited):
  visited += [node]
  for c in range(len(matrix[node])):
    if matrix[node][c] == 1 and (c not in visited):
      dfs(c, visited)
  return visited

print(*dfs(v,[]))
print(*bfs(v))
