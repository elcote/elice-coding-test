import sys
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

# DFS 를 통해 입력된 노드에서 
# 가장 멀리 갔을때의 길이를 distance 에 저장함
def DFS(node, weight):
    for i in tree[node]:
        a, b = i
        # distance 의 값이 -1인지 확인 함으로서, 
        # DFS 함수를 실행 한적이 있는 노드인지 체크후 시작
        if distance[a] == -1:
            distance[a] = weight + b
            # 재귀호출을 통해 노드에서 가장 먼 길이를 distance에 저장
            DFS(a, weight + b)

N = int(input())

# 0 번 노드는 없으므로, N+1 번 반복하여 
# 1~N 까지의 노드 모두 빈 배열로 2중배열 선언
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    parent, curNode, weight = map(int, input().split())
    #부모 노드에 자식 노드와 간선의 가중치를, 자식노드에 부모노드와 간선의 가중치를 입력
    tree[parent].append([curNode,weight])
    tree[curNode].append([parent,weight])
# print(tree)
#나올수 없는 값으로 각 노드에서 가장 먼 거리를 초기화 함
distance = [-1] * (N+1)
# 1번 노드에서 시작함으로 0으로 설정
distance[1] = 0
# 1번 노드에서 시작하여 가장 멀리 갈수 있는 값을 저장
DFS(1,0)

# 위 DFS(1,0) 을 통해 나온 
# 1번 노드로 부터 각 노드 까지의 거리를 통해 
# 가장 멀리 있는 노드의 인덱스를 찾아 해당 노드 부터 다시 DFS 시작
start = distance.index(max(distance))
# distance 초기화
distance = [-1] * (N+1)
# 시작 노드 초기화
distance[start] = 0
# 해당 start 노드부터 가장 먼 노드 탐색
DFS(start, 0)

print(max(distance))
