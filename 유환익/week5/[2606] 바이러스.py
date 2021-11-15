import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

# 그래프 공간 생성
graph = [[]*n for _ in range(n+1)]

for _ in range(m):
  a,b = map(int, input().split())

  # 각 노드간 연결관계를 만든다
  graph[a].append(b)
  graph[b].append(a)

# 바이러스 걸리게 될 수 있는 가능한 컴퓨터 수 카운트
cnt = 0 
# 방문 여부를 체크할 배열 생성 ( 0: 미방문, 1: 방문)
visited = [0] * (n+1)

# dfs를 할 함수를 정의한다.
def dfs(node):
  global cnt # 전역변수로 사용
  visited[node] = 1  # 첫 방문노드 방문 처리
  for i in graph[node]:
    if not visited[i]: # 아직 방문하지 않았다면
      dfs(i) # dfs 함수를 재귀하여 방문/탐색을 진행
      cnt += 1 # 카운트를 1 증가한다.

dfs(1)
print(cnt)

