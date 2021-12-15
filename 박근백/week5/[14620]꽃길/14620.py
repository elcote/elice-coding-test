import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]

def recur(cnt, cost):
    global min_cost
    if cnt == 3:
        min_cost = min(min_cost, cost)
        return

    for y in range(1, n-1):
        for x in range(1, n-1):
            temp = []
            for i in range(5):
                nx = x + dx[i]
                ny = y + dy[i]
                if visit[ny][nx] == 1:
                    break
                temp.append((nx, ny))
            else:
                add_cost = 0
                for nx, ny in temp:
                    visit[ny][nx] = 1
                    add_cost += board[ny][nx]
                recur(cnt + 1, cost + add_cost)
            for nx, ny in temp:
                visit[ny][nx] = 0

n = int(input())
board = []
min_cost = 3001

for _ in range(n):
    board.append(list(map(int, input().split())))

visit = [[0 for _ in range(n)] for _ in range(n)]
recur(0, 0)
print(min_cost)