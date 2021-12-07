#완전이진트리
#깊이에 따른 값들을 출력한다

import sys
input=sys.stdin.readline

K=int(input())
_input=list(map(int, input().split()))
tree=[[] for _ in range(K)]

def maketree(arr, x):#루트, 왼, 오 순으로 깊이마다 값을 넣어준다
    mid=(len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr)==1:
        return
    maketree(arr[:mid], x+1)#왼쪽 서브트리 전체를 모두 탐색하거
    maketree(arr[mid+1:], x+1)#오른쪽 서브트리를 차례대로 탐색한다

maketree(_input, 0)
for i in range(K):
    print(*tree[i])