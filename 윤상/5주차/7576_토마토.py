import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

M, N = map(int, input().split())


startTomato = []
box = []
visited = [[False] * M for _ in range(N)]
di = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque()
dayCnt = 0

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 1:
            startTomato.append((i,j))
    box.append(line)

def BFS(q):
    temp_day_q = deque()
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        temp_day_q.append((y,x))
    while temp_day_q:
        y, x = temp_day_q.popleft()
        for d in di:
            ny = y + d[0]
            nx = x + d[1]
            if 0<= nx <= M-1 and 0<= ny <= N-1 and visited[ny][nx] == False and box[ny][nx] == 0:
                q.append((ny,nx))
                box[ny][nx] = 1

for tomato in startTomato:
    q.append(tomato)

while q:
    BFS(q)
    dayCnt += 1

# print(q)

for line in box:
    if 0 in line:
        print(-1)
        break
else:
    print(dayCnt-1)

    