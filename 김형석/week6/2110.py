'''
    문제 이름 : 공유기 설치
    문제 번호 : 2110
    문제 링크 : https://www.acmicpc.net/problem/2110
'''

import sys
read = sys.stdin.readline

n, c = map(int, read().split())
houses = [int(read()) for _ in range(n)]
houses.sort()

start = 1
end = houses[-1] - houses[0]

answer = 0

while (start <= end):
    mid = (start+end)//2  # 해당 gap
    current = houses[0]
    count = 1  # 시작할때 1개

    for i in range(1, len(houses)):
        if houses[i] >= current + mid:  # gap 이상
            count += 1
            current = houses[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
