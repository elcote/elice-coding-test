'''

<완전 이진 트리>

1. 가장 처음에 상근이는 트리의 루트에 있는 빌딩 앞에 서있다.
2. 현재 빌딩의 왼쪽 자식에 있는 빌딩에 아직 들어가지 않았다면, 왼쪽 자식으로 이동한다.
3. 현재 있는 노드가 왼쪽 자식을 가지고 있지 않거나 왼쪽 자식에 있는 빌딩을 이미 들어갔다면, 현재 노드에 있는 빌딩을 들어가고 종이에 번호를 적는다.
4. 현재 빌딩을 이미 들어갔다 온 상태이고, 오른쪽 자식을 가지고 있는 경우에는 오른쪽 자식으로 이동한다.
5. 현재 빌딩과 왼쪽, 오른쪽 자식에 있는 빌딩을 모두 방문했다면, 부모 노드로 이동한다.

위와 같은 방문순서(중위 순회) -> 트리의 전체 구조를 파악한다.

★★★ 중위 순회를 정렬된 배열이라고도 한다. 알고리즘 인터뷰 Q50 ★★★


'''

import sys
input = sys.stdin.readline

# 깊이 k 입력 받기
k = int(input())

# 전위 순회 결과 입력받기
_input = list(map(int, input().split()))

# 빈 트리 2차원 배열로 할당
tree = [[] for _ in range(k)]

print(_input)
print(tree)

# 분할 정복 과정
def makeTree(arr, x):
    mid = (len(arr)//2)         # mid 번째 index를 찾고 
    print(mid)
    tree[x].append(arr[mid])    # tree 의 x 깊이에 해당되는곳에 arr[mid] 값을 넣어준다. 
    print(f'현재 tree 입니다. : {tree}')
    print(f'현재 len(arr) 입니다. : {len(arr)}')

    if len(arr) == 1:   # 마지막 리프 노드에 도달 했을 경우(len(arr)이 1인 경우)
        return          # 해당 함수를 빠져나온다.

    print(f'현재 arr[:mid] 입니다. : {arr[:mid]}')      # 왼쪽 tree 와
    print(f'현재 arr[mid+1:] 입니다. : {arr[mid+1:]}')  # 오른쪽 tree 로 나눠서 위와 같은 과정을 반복
    
    makeTree(arr[:mid], x+1)
    makeTree(arr[mid+1:], x+1)

# 1. 스타트
makeTree(_input, 0)

'''
첫번째 인수인 _input 은 전위 순회 결과 리스트 입니다. 
두번째 인수인 0 은 tree 의 index 로 활용할 것입니다.
'''

# 마지막
for i in range(k):
    print(*tree[i]) # 리스트 앞에 * 을 붙이면 [] 대괄호를 없앤 상태로 출력된다.