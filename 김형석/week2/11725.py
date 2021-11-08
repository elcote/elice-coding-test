'''
    문제 이름 : 트리의 부모 찾기
    문제 번호 : 11725
    문제 링크 : https://www.acmicpc.net/problem/11725
'''

import sys

read = sys.stdin.readline
#1,000으로 설정되어있다. 해결 방법으로는 sys.setrecursionlimit()을 사용하는 것이 있다. 
#이 함수를 사용하면, Python이 정한 최대 재귀 갚이를 변경할 수 있다. 최대 재귀 깊이를 1,000,000 정도로 크게 설정하면 런타임 에러 없이 실행 된다.
sys.setrecursionlimit(10**9);


def dfs(graph, start, parent):
    for child in graph[start]:
        if parent[child] == -1:  # 방문 안했을 경우
            parent[child] = start
            # 모두 방문할때까지 재귀
            dfs(graph, child, parent)


n = int(read())
graph = [[] for _ in range(n+1)]  # 맨 앞자리 비어있으므로 n+1개
parent = [-1 for _ in range(n+1)]

for i in range(n - 1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, parent)

for i in range(2, n+1):
    print(parent[i])
