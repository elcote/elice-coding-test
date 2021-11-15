import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
di = [(-1,0),(1,0),(0,-1),(0,1)]
sizeCnt = []
cnt = 0

for i in range(N):
    line = input()
    for c in line:
        graph[i].append(int(c))
        
def DFS(r, c):
    global cnt
    for y,x in di:
        nr = r + y
        nc = c + x
        if 0 <= nr <= N-1 and 0 <= nc <= N-1 and visited[nr][nc] == False and graph[nr][nc] == 1:
            visited[nr][nc] = True
            cnt += 1
            DFS(nr, nc)

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1 and visited[i][j] == False:
            cnt += 1
            visited[i][j] = True
            DFS(i,j)
            sizeCnt.append(cnt)
            cnt = 0

print(len(sizeCnt))
for size in sizeCnt:
    print(size)
