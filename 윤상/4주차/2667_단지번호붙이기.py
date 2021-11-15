import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
di = [(-1,0),(1,0),(0,-1),(0,1)]
totalcnt = 0
sizeCnt = []
for i in range(N):
    line = input()
    for c in line:
        graph[i].append(int(c))
# for sub in graph:
#     print(sub)
def DFS(r, c, idx):
    if visited[r][c] == True:
        return
    else:
        visited[r][c] = True
        sizeCnt[idx] += 1
        for y,x in di:
            nr = r + y
            nc = c + x
            if 0 <= nr <= N-1 and 0 <= nc <= N-1 and visited[nr][nc] == False and graph[nr][nc] == 1:
                DFS(nr, nc, idx)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1 and visited[i][j] == False:
            sizeCnt.append(0)
            DFS(i,j,totalcnt)
            totalcnt += 1
# for visit in visited:
#     print(visit)

print(totalcnt)
for size in sizeCnt:
    print(size)
