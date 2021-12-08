'''
    문제 이름 : 토마토 
    문제 번호 : 7576
    문제 링크 : https://www.acmicpc.net/problem/7576
'''

'''
1 = 익은 🍅
0 = 안 익은 🍅
-1 = 🍅 없음
'''
import sys
from collections import deque;
read = sys.stdin.readline;

que = deque([]) #익은 토마토 위치 담을 큐
m,n = map(int,read().split())
field = [list(map(int,read().split())) for _ in range(n)]

'''
[dx[0],dy[0]] = 왼쪽 방향
[dx[1],dy[1]] = 오른쪽 방향
[dx[2],dy[2]] = 아래쪽 방향
[dx[3],dy[3]] = 위쪽 방향
'''
dx,dy = [-1,1,0,0],[0,0,-1,1]
# 정답
answer = 0

for i in range(n):
    for j in range(m):
        #익은 토마토의 좌표
        if field[i][j] == 1:
            que.append([i,j])


def bfs():
    #큐가 빌때까지
    while que:
        #처음 토마토의 좌표
        x,y = que.popleft();
        #처음 토마토의 왼,오,위,아 좌표
        for i in range(4):
            #방향 리스트 사용
            nx,ny = dx[i] + x,dy[i] +y
            if 0<= nx <n and 0 <= ny < m and field[nx][ny] == 0:
                # ! 이부분 잘못 작성해서 오류났었음
                field[nx][ny] = field[x][y] +1   #토마토 익히기
                que.append([nx,ny]) #익힌 토마토 다시 넣어줌
bfs()
for i in field:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer,max(i))

print(answer -1)