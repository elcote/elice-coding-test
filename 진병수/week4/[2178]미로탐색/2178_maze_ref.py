'''
https://www.youtube.com/watch?v=7C9RgOcvkvo&t=1645s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98

동빈나 <이것이 코딩테스트다> - [미로 탈출 문제] 를 참고한 코드와 아이디어입니다. 

백준 2178_[미로탐색 문제]와 '완전히' 같은 문제 입니다.

- 입력 예시 -
5 6
101010
111111
000001
111111
111111

- 출력 예시 -
10

'''

# from collections import deque               # deque 라이브러리를 호출할 필요가 있다는 점 기억해주세요!

n, m = map(int, input().split())            # n, m 을 공백을 기준으로 구분하여 입력

graph = []
for i in range(n):
    graph.append(list(map(int, input())))   # 2차원 리스트의 맵 정보 입력받기

print(graph)

dx = [-1, 1, 0, 0]                          # 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = []                              # 그냥 queue 로 해보자
    queue.append((x, y))                    # 시작 지점 append

    while queue:                            # queue 가 완전히 비어있을 때까지 반복
        print(f"현재 queue : {queue} 입니다.") 
        x, y = queue.pop(0)

        for i in range(4):                  # 현재 좌표(x, y)에서 4가지 방향으로 위치 확인(시작 노드와 연결된 노드 확인)
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 미로 찾기 공간을 벗어난 경우 무시
                continue
            
            if graph[nx][ny] == 0:                      # 벽인 경우 무시
                continue

            if graph[nx][ny] == 1:                      # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
                                                        # graph[nx][ny] == 1 이란 의미는 아직 방문하지 않았다는 의미 2, 3, 4.. 등의 경우 방문했다는 의미
                graph[nx][ny] = graph[x][y] + 1         # graph[nx][ny] 좌표를 방문하면 기존 graph[x][y] 좌표에 1을 더한 값을 할당
                # print(f"현재 graph : {graph} 입니다.")                                   
                queue.append((nx, ny))
                # print(f"현재 [nx][ny] : ({nx}, {ny}) 입니다.")
                # print(f"현재 graph[nx][ny] : {graph[nx][ny]} 입니다.\n")
    
    return graph[n-1][m-1]                              # 가장 오른쪽 아래까지의 최단거리 반환

print(bfs(0, 0))                                        # bfs를 수행하여 return 된 graph[n-1][m-1] 을 출력