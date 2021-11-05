'''
    문제 이름 : 카드 2
    문제 번호 : 2164
    문제 링크 : https://www.acmicpc.net/problem/2164
'''

import sys
from collections import deque

# 수행하는 동작 : 버리고 제일 위에 있는 카드 제일 아래로 옮김
# 위 동작을 1개 남을때까지 수행

n = int(sys.stdin.readline())
deq = deque([i for i in range(1, n+1)])

# 1개 남을때까지 수행
while len(deq) != 1:
    # 한개 버리고
    deq.popleft()

    # 제일 아래 카드 제일 위로 삽입
    tmp = deq.popleft()
    deq.append(tmp)

# 언패킹
print(*deq)

#디폴트 딕트
'''

'''