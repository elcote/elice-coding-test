from copy import deepcopy
import sys
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lab = []
virus = []
freeWay = []
di = [(-1,0),(1,0),(0,-1),(0,1)]
wallBuilt = [[False] * M for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(M):
        if line[j] == 2:
            virus.append((i,j))
        if line[j] == 0:
            freeWay.append((i,j))
    lab.append(line)

def DFS(vir, tmpLab, visited):
    visited[vir[0]][vir[1]] = True
    tmpLab[vir[0]][vir[1]] = 2
    for d in di:
        new_y = vir[0] + d[0]
        new_x = vir[1] + d[1]
        if 0 <= new_y <= N-1 and 0 <= new_x <= M-1 and tmpLab[new_y][new_x] == 0 and visited[new_y][new_x] == False:
            DFS((new_y, new_x), tmpLab, visited)

def countZeros(labs):
    summ = 0
    for lab in labs:
        summ += lab.count(0)
    return summ

def buildWall():
    wallBuilding = combinations(freeWay,3)
    max_rooms = 0
    for walls in wallBuilding:
        tmpLab = deepcopy(lab)
        for wall in walls:
            tmpLab[wall[0]][wall[1]] = 1
        visited = [[False] * M for _ in range(N)]
        for vir in virus:
            DFS(vir, tmpLab, visited)
        res = countZeros(tmpLab)
        if max_rooms < res:
            max_rooms = res
    return max_rooms
                
print(buildWall())
