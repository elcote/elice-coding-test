
"""
    문제 이름: 효율적인 해킹
    문제 번호: 1325
    문제 링크: https://www.acmicpc.net/problem/1325
    난이도: Silver II
    태그: 너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

    - 문제 - 
    해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 
    김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
    
    이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, 
    A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
    
    이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 
    한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

    - 입력 -
    첫째 줄에, N과 M이 들어온다. 
    N은 10,000보다 작거나 같은 자연수, 
    M은 100,000보다 작거나 같은 자연수이다. 
    
    둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. (이 경우, B가 부모노드, A가 자식노드)
    컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

    - 출력 -
    첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
"""

"""
해당 문제의 graph 형태를 dict 로 할 경우 시간초과가 발생합니다.
또한, bfs 가 아닌 dfs 형태로 순회할 경우 시간초과가 발생합니다.
백준 python3 와 pypy3 의 차이를 모르겠습니다.
"""

import sys

def input(): 
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

dict_graph = {i:[] for i in range(1, n+1)}          # dict_graph = {} 로 비어있는 dict로 선언시 백준에서 key error 발생!!!

for _ in range(m):
    s, e = map(int, input().split())
    dict_graph[e] = dict_graph.get(e, []) + [s]     # {부모노드:[자식노드]} 형태로 graph 정보를 입력합니다.

print(f"dict_graph 입니다. : {dict_graph}")

def bfs(v):                                         # bfs(큐를 이용한 반복문)
    visited = [v]
    queue = [v]
    cnt = 1
    while queue:
        v = queue.pop(0)
        for w in dict_graph[v]:
            if w not in visited:
                queue.append(w)
                visited.append(w)
                cnt += 1
    return cnt                                      # ★ 여기서, bfs 의 return 값은 자기 자신을 포함한 연결된 노드의 개수입니다. ★

_max = 0        # cnt 값이 최대인 경우 _max 에 할당해줄 것임. 
answer = []     # cnt 값이 최대이거나 최대와 같은 노드를 answer 리스트에 넣어 줄 것임.

for i in range(1, n+1):
    print(f"현재 bfs 시작노드{i}의 경우 연결된 노드의 개수는 {bfs(i)}")
    
    result = bfs(i)                     # 여기서 result 는 어떠한 자기 자신을 포함하며, 노드에 연결된 노드의 개수를 말합니다.

    if result > _max:                   # 현재 _max 보다 result 값이 크다면
        _max = result                   # result 를 _max 로 할당하고
        answer = [i]                    # 현재 노드 i 를 answer 에 넣어줍니다.

    elif result == _max:                # _max 와 result 가 같다면
        answer.append(i)                # 현재 노드 i 를 answer 에 append 해줍니다.

    print(f"현재 result는 {result}")
    print(f"현재 answer는 {answer}\n")
    
print(*answer)
