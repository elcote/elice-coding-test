'''
    문제 이름 : N번째 큰 수
    문제 번호 : 2075
    문제 링크 : https://www.acmicpc.net/problem/2075
'''

import sys
import heapq

read = sys.stdin.readline

N = int(read())
result = []

for i in range(N):
    nums = list(map(int, read().split()))

    if not result:
        # 첫 1회 실행
        for num in nums:
            heapq.heappush(result, num)
            # 현재 result = N개 들어가 있음

    # 이후 횟수 여기서 실행
    else:
        for num in nums:
            # result의 가장 작은 값이 num보다 작은 경우 교체
            # 이렇게 되면 길이가 N으로 유지됨
            if result[0] < num:
                heapq.heappush(result, num)
                heapq.heappop(result)

print(result[0])

# 메모리 초과..
'''
import sys

read = sys.stdin.readline

N = int(read())
result = []

for i in range(N):
    nums = list(map(int, read().split()))
    for j in nums:
        result.append(j)

result.sort(reverse=True)
print(result[N-1])
'''
