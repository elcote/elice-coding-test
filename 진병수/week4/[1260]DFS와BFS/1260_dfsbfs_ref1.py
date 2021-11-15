'''
dfs 재귀 구현 예제입니다.
'''

# graph = {                       # graph 정보
#     1: [2, 3, 4],
#     2: [5],
#     3: [5],
#     4: [],
#     5: [6, 7],
#     6: [],
#     7: [3],
# }

# visited = []                    # 방문 정보

# def recursive_dfs(start):       # dfs 함수 정의(★ 시작 지점만 인수로 넣어줘도 된다. ★)
#     visited.append(start)       # (append 과정)

#     for now in graph[start]:    # 시작 지점과 연결된 다른 노드를 순회           (for 과정)
#         if now not in visited:  # 연결된 다른 노드가 방문 정보에 없으면         (if 과정)
#             recursive_dfs(now)  # 연결된 다른 노드를 시작 노드로 잡고 재귀      (recursive 과정)
#     return visited              # 모든 재귀가 끝날때 방문 정보를 return 한다.

# print(recursive_dfs(1))         # 시작 지점을 넣는다.

############################################

'''
dfs 재귀 구현 예제입니다.
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

visited = []

def dfs_recursive(graph, start):    # ★ 시작 노드를 인자로 넣는건 필수, 나머지는 선택 ★
    
    if start in visited:            # 이미 방문한 노드라면 탐색 종료(if 과정)
        return
    
    visited.append(start)           # 방문 표시                     (append 과정)
                                    # 인접 정점들에 대해 재귀 호출
    for now in graph[start]:        # 인접 정점을 순회              (for 과정)        
        dfs_recursive(graph, now)   # 인접 정점을 시작 지점으로 삼고 재귀 (recursive 과정)

    return visited

print(dfs_recursive(graph, 1))      # graph 정보와 시작지점을 매개변수로 넣는다.