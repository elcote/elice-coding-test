from collections import deque

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
#상자그리기
queue = deque([])
#bfs를 사용할때에는 pop, append가 빠른 deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

res = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])
#queue에 익은 토마토가 있는 자리를 넣어준다
def bfs():
    while queue:
        x, y = queue.popleft()#처음 토마토 위치
        for i in range(4):#처음꺼낸 토마토의 4방향을 모두 익은상태로
            nx, ny = dx[i] + x, dy[i]+ y
            #좌표크기가 해당좌표를 넘어가지않고 안익은 상탤라면
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny]==0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

bfs()
for i in matrix:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res, max(i))

#처음시작을 1로시작했기에 -1
print(res-1)