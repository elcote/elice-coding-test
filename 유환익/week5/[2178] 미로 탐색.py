import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향을 정한다 (위, 아래, 왼쪽, 오른쪽)
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()

  # 큐에 초기값을 넣는다.
  queue.append((x,y))

  # 큐가 비어 있지 않을 동안
  while queue:

    # 
    x,y = queue.popleft()

    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      # 벽이 있으면 갈 수 없다
      if graph[nx][ny] == 0:
        continue

      # 벽이 아니라면 진행 가능하다.
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
  
  # 마지막 값에서 이동한 개수를 리턴한다.
  return graph[n-1][m-1]

# 시작지점에서 시작하도록 bfs함수를 호출한다.
print(bfs(0,0))
  