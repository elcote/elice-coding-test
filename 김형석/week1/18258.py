'''
    문제 이름 : 큐2
    문제 번호 : 18258
    문제 링크 : https://www.acmicpc.net/problem/18258
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
# deque 사용한 이유 : 양쪽에서 접근이 가능해서 속도가 더 빠르고 사용하기 쉬움
deq = deque([])

for i in range(n):
    # readlines 쓰는 실수 조심..
    arr = sys.stdin.readline().split()
    command = arr[0]  # 명령어
    if command == "push":
        deq.append(arr[1])
    elif command == "pop":
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif command == "size":
        print(len(deq))
    elif command == "empty":
        if not deq:
            print(1)
        else:
            print(0)
    elif command == "front":
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif command == "back":
        if not deq:
            print(-1)
        else:
            print(deq[-1])
