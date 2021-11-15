import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
MAP = [[] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
di = [(1,0),(-1,0),(0,1),(0,-1)]
cnt = [[0] * M for _ in range(N)]

for i in range(N):
    line = input()
    for c in line:
        MAP[i].append(int(c))

def BFS(r,c):
    q = deque()
    q.append((r,c))
    visited[r][c] = 1
    while q:
        org_r, org_c = q.popleft()
        for y,x in di:
            new_r = org_r + y
            new_c = org_c + x
            # print(new_r, new_c)
            if 0<= new_c <= M-1 and 0 <= new_r <= N-1 and MAP[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                q.append((new_r, new_c))
                cnt[new_r][new_c] = cnt[org_r][org_c] + 1
            # for i in cnt:
            #     print(i)
            # print()
cnt[0][0] = 1
BFS(0,0)
print(cnt[N-1][M-1])