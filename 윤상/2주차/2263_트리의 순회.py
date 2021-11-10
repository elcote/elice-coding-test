import sys
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
preOrder= []
position = [0 for i in range(N+1)]
for i in range(N):
    position[inOrder[i]] = i

# 1. postOrder 의 마지막 노드 => 루트노드
# 2. inOrder 에서 루트노드를 찾아서 왼쪽서브트리, 오른쪽서브트리 로 나눔
# 3. inOrder 에서 왼쪽 서브트리와 오른쪽서브트리를 나눈 인덱스를(루트 노드를 제외한) 기준으로
# 4. postOrder 또한 나누면 실제 트리상 왼쪽 서브트리와 오른쪽 서브트리가 나뉘어짐
# 1 ~ 4 번 계속 반복


# 각 inOrder 와 postOrder의 시작 그리고 끝을 넘겨줌
# 7 4 8 2 1 5 3 6 => inOrder
# 7 8 4 2 5 6 3 1 => postOrder
def PREORDER(instart, inend, poststart, postend):
    if instart > inend or poststart > postend:
        return
    preOrder.append(postOrder[postend])
    # inOrderRoot = inOrder.index(postOrder[postend])
    inOrderRoot = position[postOrder[postend]]
    leftSubTreeSize = inOrderRoot-instart
    PREORDER(instart, inOrderRoot-1, poststart, poststart + leftSubTreeSize -1)
    PREORDER(inOrderRoot+1, inend, poststart + leftSubTreeSize, postend-1)

PREORDER(0,len(inOrder)-1, 0, len(postOrder)-1)
print(*preOrder)