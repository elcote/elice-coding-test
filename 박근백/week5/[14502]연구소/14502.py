import sys, copy
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(v, f, s, t):
    copy_board = copy.deepcopy(board)
    q = deque(v)
    count = 0

    for a, b in (f, s, t):
        copy_board[b][a] = 1

    while q:
        x, y = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if copy_board[ny][nx] == 0:
                    copy_board[ny][nx] = 2
                    q.append((nx, ny))

    return count - len(v)

n, m = map(int, input().split())
board = []
virus = []
zero = []
max_area = 0

for y in range(n):
    line = list(map(int, input().split()))
    board.append(line)
    for x in range(len(line)):
        if line[x] == 2:
            virus.append((x, y))
        if line[x] == 0:
            zero.append((x, y))

for i in range(len(zero)):
    for j in range(i + 1, len(zero)):
        for k in range(j + 1, len(zero)):
            infection_area = bfs(virus, zero[i], zero[j], zero[k])
            max_area = max(max_area, len(zero) - 3 - infection_area)

print(max_area)



