import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(input().strip()))

def bfs(a, b):
    q = deque([(a, b, 1)])
    board[b][a] = '0'

    while q:
        x, y, now = q.popleft()
        if x == m - 1 and y == n - 1:
            print(now)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == '1':
                    board[ny][x] = '0'
                    q.append((nx, ny, now + 1))

bfs(0, 0)


