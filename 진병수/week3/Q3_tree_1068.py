'''

<트리>

트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 

그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 

노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

-입력-
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 

둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 
만약 부모가 없다면 (루트) -1이 주어진다.

셋째 줄에는 지울 노드의 번호가 주어진다.


-출력-
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

'''

import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    print(f'잘린 node 번호는 : {num} 입니다.')
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
print(f'tree 의 정보입니다.: {arr} 입니다.')

k = int(input())    # 자를 node 번호를 입력합니다.
count = 0

dfs(k, arr)         # k 노드를 기준으로 dfs를 돌아 다 잘라버린다 (-2로 바꾼다.)

print(f'자른 후 tree 의 정보입니다.: {arr} 입니다.')

count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:   # 여기서 리프 노드를 판단해야 한다. 
                                        # 해당 i 가 arr에 있다는 의미는 그 i를 부모로 하는 자식 노드가 있다는 말 (i가 부모노드라는 말)
                                        
        print(f'i는 {i ,} i not in arr 의 정보입니다.: {i not in arr} 입니다.')
        
        count += 1                      # 리프 노드의 갯수를 카운트 해준다.
print(count)