import sys
sys.setrecursionlimit(10**9) # 재귀횟수 초과를 방지하기 위해 리미트를 늘린다.

def input():
  return sys.stdin.readline().rstrip()

def dfs(y,x,cnt):
  
  # 첫번째 시작 노드는 1로 방문 처리하고 
  visited[y][x] = 1
  
  # 1을 카운트한다.
  cnt += 1

  # 상하좌우 4방향을 탐색할 반복문
  for i in range(4):
    # 다음 방문 : 위, 아래
    ny = y+dy[i]
    # 다음 방문 : 오른쪽, 왼쪽
    nx = x+dx[i]
    
    # 단지 그래프의 범위를 초과하지 않도록 한다.
    if 0 <= ny < n and 0 <= nx < n:
      # 그래프 내에 이동할 공간이 있고, 다음 이동 좌표가 방문되지 않았다면
      if graph[ny][nx] and not visited[ny][nx]:
        cnt = dfs(ny,nx,cnt)
  return cnt

# 숫자 n을 입력 받는다
n = int(input())

# 그래프 생성 n의 수만큼 노드를 생성한다.
graph = [[int(x) for x in input()] for _ in range(n)]

# 노드 방문을 체크할 공간을 n의 수만큼 생성
visited = [[0 for _ in range(n)] for _ in range(n)]

# 위, 아래
dy = [-1,0,1,0]
# 오른쪽, 왼쪽
dx = [0,1,0,-1]

# 결과로 리턴할 배열 선언
result = []
# 단지 개수 카운터
complex = 0

# 그래프 내를 순회하며 (x,y 축)
for i in range(n):
  for j in range(n):
    
    # 그래프에 갈 공간이 존재하고, 아직 방문하지 않았다면
    if graph[i][j] and not visited[i][j]:

      # 각 단지내 집수를 result 리스트에 넣는다 
      # (dfs함수를 호출해, 인자로 방문할 x,y 좌표 그리고 단지 내 집을 카운트할 cnt를 넘겨줌)
      result.append(dfs(i,j,0))

      # 단지 단위로 카운트 한다
      complex += 1

# 이어진 단지의 총 개수를 출력하고
print(complex)

# 단지 내 집 수를 오름 차순으로 정렬하여 차례대로 출력
for r in sorted(result):
  print(r)