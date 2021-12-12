import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
maps = []

for _ in range(N):
    line = list(map(int, input().split()))
    maps.append(line)
# print(maps)

ans = 0
di = [(-1,0),(1,0),(0,-1),(0,1)]

def DFSforThree(i, j, cur, count):
    global tmp
    if count >= 3:
        tmp = max(tmp, cur)
        return
    for d in di:
        ni = i + d[0]
        nj = j + d[1]
        if 0<= ni < N and 0 <= nj < M and visited[ni][nj] == False:
            visited[ni][nj] = True
            DFSforThree(ni, nj, cur + maps[ni][nj], count + 1)
            visited[ni][nj] = False

def fourDirection(i,j, cur):
    global tmp
    for d in di:
        ni = i + d[0]
        nj = j + d[1]
        if 0<= ni < N and 0 <= nj < M:
            cur += maps[ni][nj]
    values = [cur] * 4
    # print(values)
    idx = 0
    for d in di:
        ni = i + d[0]
        nj = j + d[1]
        if 0<= ni < N and 0 <= nj < M:
            values[idx] -= maps[ni][nj]
        idx += 1
    tmp = max(tmp, max(values))

visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):            
        tmp = 0
        visited[i][j] = True
        DFSforThree(i,j,maps[i][j],0)
        visited[i][j] = False
        fourDirection(i,j,maps[i][j])
        ans = max(ans, tmp)

print(ans)