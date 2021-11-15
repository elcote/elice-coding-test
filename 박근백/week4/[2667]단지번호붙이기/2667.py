import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = []

for _ in range(n):
    board.append(list(input().strip()))

results = []

def bfs(a, b, val):
    q = deque([(a, b)])
    board[b][a] = '0'
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if board[ny][nx] == val:
                    board[ny][nx] = '0'
                    q.append((nx, ny))
    return cnt

for y in range(n):
    for x in range(n):
        if board[y][x] != '0':
            results.append(bfs(x, y, board[y][x]))

results.sort()
print(len(results))
for el in results:
    print(el)