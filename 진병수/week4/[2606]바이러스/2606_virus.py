
"""
    문제 이름: 바이러스
    문제 번호: 2606
    문제 링크: https://www.acmicpc.net/problem/2606
    난이도: Silver III
    태그: 너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

    신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
    한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
    예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
    1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 
    2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
    하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

    어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
    컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
    1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

    - 입력 -
    첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
    둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
    이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

    - 출력 -
    1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
    => ★ 1번 컴퓨터를 제외한 연결되어 있는 컴퓨터의 개수를 출력하라 ★
    => ★ visted 에 append 되어 있는 수 - 1 을 구하면 정답이 된다. ★
"""

'''
- 예제 입력  - 
7
6
1 2
2 3
1 5
5 2
5 6
4 7

- 예제 출력  -
4
'''

import sys 

def input(): 
    return sys.stdin.readline().rstrip()

dic={}
n = int(input())                     # n 으로 컴퓨터의 수를 입력합니다.
m = int(input())                     # m 으로 직접 연결되어 있는 컴퓨터 쌍의 수를 입력합니다.

for i in range(n):                   # 입력된 노드의 개수만큼 dict(사전) 안에 set(집합) 공간을 만들어준다.
    dic[i+1] = set()                 # {노드번호: set()} 형태로 공간이 생성됩니다.

print(f"입력 전 dic 은 : {dic}")

for j in range(m):                   # 입력된 연결관계 숫자만큼 입력하고 그만큼 반복하면서
    a, b = map(int,input().split())  # graph 에 대한 정보를 하나씩 입력받는다.
    dic[a].add(b)                    # {노드번호:{연결된 노드, 연결된 노드}, } 형태로 생성됩니다. (dict-dict 형태)
    dic[b].add(a)

print(f"입력 후 dic 은 : {dic}")

# dfs 정의(재귀 이용)
def dfs(start):                      # dfs 의 인수로는 시작노드만 넣어줘도 됩니다.
    for i in dic[start]:
        # print(f"현재 start 노드는 {start} start에 연결된 노드는 {i} 입니다.")
        
        if i not in visited:
            visited.append(i)
            # print(f"현재 visited는 {visited} 입니다.\n")
            dfs(i)

visited = []
dfs(1)

print(len(visited)-1)                # 시작지점노드를 제외한 연결된 다른 노드의 개수를 출력