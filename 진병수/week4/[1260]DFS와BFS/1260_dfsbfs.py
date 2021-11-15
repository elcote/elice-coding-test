
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
import sys

def input():
    return sys.stdin.readline()

n, m, v = map(int, input().split())     # n: 정점의 개수(인덱스 번호로 대체), m: 간선의 개수, v: 시작 노드

dict_graph = {i:[] for i in range(1, n+1)}      # dict_graph = {} 로 비어있는 dict로 선언시 백준에서 key error 발생!!!

for i in range(m):
    a, b = map(int, input().split())
    dict_graph[a] = dict_graph.get(a, []) + [b] # dict - list 형태로 graph 정보를 입력
    dict_graph[b] = dict_graph.get(b, []) + [a]
    dict_graph[a].sort()                        # 문제에서 요구하는 사항 때문에, sort 과정을 반드시 해줘야한다.
    dict_graph[b].sort()

# print(f"현재 graph 입니다. {dict_graph}")

visited = []             # 방문 기록을 확인하기 위한 visited 리스트

# print(f"현재 visited 입니다. {visited}")

def dfs(v):                             # dfs(재귀 이용)
    visited.append(v)
    
    # print(f"현재 시작점 v 입니다. {v}")
    # print(f"현재 visited 입니다. {visited}\n")
    
    for w in dict_graph[v]:
        if w not in visited:
            dfs(w)
    return visited

def bfs(v):             # bfs(큐를 이용한 반복문, deque 자료구조를 이용합니다.)
    visited = [v]
    queue = [v]
    while queue:
        v = queue.pop(0)
        for w in dict_graph[v]:
            if w not in visited:
                queue.append(w)
                visited.append(w)
    return visited

print(*dfs(v))
print(*bfs(v))

