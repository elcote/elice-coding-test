'''
https://www.youtube.com/watch?v=7C9RgOcvkvo&t=1645s&ab_channel=%EB%8F%99%EB%B9%88%EB%82%98

동빈나 <이것이 코딩테스트다> - [음료수 얼려 먹기 문제] 를 참고한 코드와 아이디어입니다. 

백준 2178_[단지번호붙이기]와 '거의 유사한' 문제 입니다.

- 입력 예시 -
4 5 
00110
00011
11111
00000

- 출력 예시 -
3

'''

n, m = map(int, input().split())        # n, m 을 공백 기준으로 구분하여 입력 받기
graph = []

for i in range(n):  # n줄에 걸쳐서 2차원 리스트의 맵 정보를 입력 받습니다.
    graph.append(list(map(int, input())))

    # 이때 입력은 공백 없이 0과 1로 구성된 문자열 형태로 주어지기 때문에
    # 한 줄을 입력 받은 다음에 각 원소를 정수형으로 바꿔서
    # 다시 리스트 형태로 만들어 줍니다.
    # 모든 원소가 0 또는 1인 정수 리스트가 들어가 집니다.

def dfs(x, y):                                      # dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문

    if x <= -1 or x >= n or y <= -1 or y >= m:      # 주어진 범위를 벗어나는 경우 즉시 종료
        return 0
    
    if graph[x][y] == 0:                            # 현재 노드를 아직 방문하지 않았더라면
        graph[x][y] = 1                             # 해당 노드 방문 처리,★ 스타팅 포인트를 하나만 넣어주면 연결된 모든 0 들이 1로 바뀐다. ★

        dfs(x-1, y)                                 # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x, y-1)
        dfs(x+1 ,y)
        dfs(x, y+1)
        return True

    return 0

result = 0

for i in range(n):              # 모든 좌표를 돌면서 확인 작업
    for j in range(m):
        if dfs(i, j) == True:   # 스타팅 포인트를 집어넣고 return 된 값이 1이라면(얼음 덩이 한개 완성)
            
            # print(f"(i, j) 는 {i}, {j}")
            # print(f"graph 는 {graph}")
            
            result += 1         # 그때 카운트를 진행하도록 합니다.
print(result)


