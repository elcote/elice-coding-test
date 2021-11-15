'''
dfs(스택을 이용한 반복)
bfs(큐를 이용한 반복)
코드 비교 예제입니다.
'''

graph = {                       # graph 정보
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

def iter_dfs(v):
    visited = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited

def iter_bfs(v):
    visited = [v]
    queue = [v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited

print(iter_dfs(1))
print()
print(iter_bfs(1))