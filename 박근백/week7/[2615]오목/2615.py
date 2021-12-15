import sys
input = sys.stdin.readline
from collections import deque

board = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def check(a, b, num, d):
    q = deque()
    q.append((a, b))
    count = 0
    path = []
    while q:
        x, y = q.popleft()
        count += 1
        path.append((x, y))
        for i in [d, (d + 4) % 8]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 19 and 0 <= ny < 19:
                if board[ny][nx] == num and (nx, ny) not in path:
                    q.append((nx, ny))
    return count, path

for _ in range(19):
    board.append(list(map(int, input().split())))

for y in range(19):
    for x in range(19):
        if board[y][x] != 0:
            for i in range(8):
                c, p = check(x, y, board[y][x], i)
                if c == 5:
                    p.sort(key=lambda x: x)
                    print(board[y][x])
                    print(p[0][1] + 1, p[0][0] + 1)
                    exit()

print(0)

