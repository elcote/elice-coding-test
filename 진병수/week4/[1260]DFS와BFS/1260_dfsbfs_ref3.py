
"""
    문제 이름: DFS와 BFS
    문제 번호: 1260
    문제 링크: https://www.acmicpc.net/problem/1260
    난이도: Silver II
    태그: 너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

    - 문제 -
    그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
    단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
    더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

    - 입력 -
    첫째 줄에 
    정점의 개수 N(1 ≤ N ≤ 1,000), 
    간선의 개수 M(1 ≤ M ≤ 10,000), 
    탐색을 시작할 정점의 번호 V가 주어진다. 
    
    다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
    어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

    - 출력 -
    첫째 줄에 DFS를 수행한 결과를, 
    그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
    V부터 방문된 점을 순서대로 출력하면 된다.

"""
from collections import  deque

n, m, v = map(int, input().split())     # n: 정점의 개수(인덱스 번호로 대체), m: 간선의 개수, v: 시작 노드

graph = [[] for _ in range(n + 1)]      # 빈 리스트로 graph 를 만든다. 0번 ~ n번 노드생성

for i in range(m):                      # 간선의 개수만큼 graph 정보를 입력받는다.
    a, b = map(int, input().split())    
    graph[a].append(b)
    graph[b].append(a)

print(f"현재 graph 입니다. {graph}")

visited = [False] * (n + 1)             # 방문 기록을 확인하기 위한 visited 리스트

print(f"현재 visited 입니다. {visited}")

def dfs(graph, v, visited):             # dfs(재귀 이용)
    visited[v] = True
    print(f"현재 시작점 v 입니다. {v}")
    print(f"현재 visited 입니다. {visited}\n")
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):             # bfs(큐를 이용한 반복문, deque 자료구조를 이용합니다.)
    visited = [False] * (n + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v, visited)
print()
bfs(graph, v, visited)

