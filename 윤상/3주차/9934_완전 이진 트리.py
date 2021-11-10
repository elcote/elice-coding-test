import sys
def input():
    return sys.stdin.readline().rstrip()

K = int(input()) # 완전 이진 트리의 깊이

inOrder = list(map(int,input().split()))
Tree = [[] for _ in range(K)]

def DFS(arr,depth):
    if len(arr) == 1:
        Tree[depth].append(arr[0])
        # return
    else:
        mid = len(arr)//2
        Tree[depth].append(arr[mid])
        DFS(arr[:mid], depth+1)
        DFS(arr[mid+1:], depth+1)
DFS(inOrder,0)
for nodes in Tree:
    print(*nodes)