
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
    
    둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 
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
from collections import defaultdict, deque

def input(): 
    return sys.stdin.readline().rstrip()

arr = defaultdict(list)
n, m = map(int, input().split())

for _ in range(m):
    s, e = map(int, input().split())
    arr[e].append(s)

def bfs(x):
    visited = [False]*(n+1)
    visited[x] = True
    queue = deque([x])
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt

_max = 0
answer = []

for i in range(1, n+1):
    
    result = bfs(i)
    if result > _max:
        _max = result
        answer = [i]
    elif result == _max:
        answer.append(i)
    
print(*answer)
