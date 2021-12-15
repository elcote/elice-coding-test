import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

pos = [
    [(0, 0), (0, 1), (0, -1), (1, 0)],
    [(0, 0), (0, 1), (0, -1), (-1, 0)],
    [(0, 0), (1, 0), (-1, 0), (0, 1)],
    [(0, 0), (1, 0), (-1, 0), (0, -1)]
]

def dfs(x, y, count, val):
    global ans
    if count >= 3:
        if val > ans:
            ans = val
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                dfs(nx, ny, count+1, val + board[ny][nx])
                visit[ny][nx] = 0

def oper(x, y):
    global ans
    for i in range(4):
        tmp = 0
        for dx, dy in pos[i]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n:
                tmp += board[ny][nx]
            else:
                break
        if tmp > ans:
            ans = tmp

n, m = map(int, input().split())
board = []
ans = 0
visit = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        visit[y][x] = 1
        dfs(x, y, 0, board[y][x])
        visit[y][x] = 0
        oper(x, y)
print(ans)