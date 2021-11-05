'''
    문제 이름 : 이중 우선순위 큐
    문제 번호 : 7662
    문제 링크 : https://www.acmicpc.net/problem/7662
'''

import sys
import heapq

read = sys.stdin.readline
t = int(read())

minheap = []  # 최소 힙
maxheap = []  # 최대 힙

result = []

for i in range(t):
    n = int(read())  # 입력 데이터의 수
    for _ in range(n):
        command = list(read().rstrip().split())
        cmd_num = int(command[1])

        if command[0] == 'I':
            heapq.heappush(minheap, cmd_num)
            heapq.heappush(maxheap, (-cmd_num, cmd_num))
        elif command[0] == 'D':
            # 최댓값 삭제
            if cmd_num > 0:
                print(heapq.heappop(maxheap)[1])
            # 최솟값 삭제
            else:
                print(heapq.heappop(minheap))

if len(heap) == 0:
    print("EMPTY")
else:
    print(heap[-1]+" "+heap[0])
