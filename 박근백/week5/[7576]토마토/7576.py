import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(t):
    q = deque(t)
    cnt = 0
    while q:
        length = len(q)
        cnt += 1
        while length:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if board[ny][nx] == 0:
                        board[ny][nx] = 1
                        q.append((nx, ny))
            length -= 1

    return cnt - 1

m, n = map(int, input().split())

board = []
tomato = []

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(len(line)):
        if line[x] == 1:
            tomato.append((x, y))


ans = bfs(tomato)
zero_cnt = 0

for line in board:
    zero_cnt += line.count(0)

if not zero_cnt:
    print(ans)
else:
    print(-1)









