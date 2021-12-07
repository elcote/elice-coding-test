import sys

def check(i, j, visited):
    for idx in range(4):
        ni = i + d[idx][0]#상하좌우에 방문했다면 False
        nj = j + d[idx][1]
        if(ni, nj) in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer:return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N-1):#0번째 인덱스에서는 꽃이 자랄수없기때문에 1부터
            for j in range(1, N-1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp=[(i, j)]
                    temp_cost=fields[i][j]#현재위치의 땅값
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni, nj))#상하좌우의 좌표를 append
                        temp_cost += fields[ni][nj]#4방향 땅값의 합
                    dfs(visited + temp, total+temp_cost)
#visited+temp = 심은곳, 4방향의 좌표를 더한값
#total+temp_cost = 심은곳의 땅값
#이 2가지 값을 dfs로 넘겨준다
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer=int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dfs([], 0)
print(answer)
