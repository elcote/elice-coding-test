'''
    문제 이름 : 요세푸스 문제
    문제 번호 : 1158
    문제 링크 : https://www.acmicpc.net/problem/1158
'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())  # 입력 받음

circle = deque([i for i in range(1, n+1)])  # deque 사용 사람들 넣어줌

result = []  # 빼준 사람들 담을 리스트

print("<", end="")
for i in range(n):
    # deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
    circle.rotate(1-k)

    if i != n-1:
        print(circle.popleft(), end=', ')
    else:  # 마지막 원소일시 , 없이 출력
        print(circle.popleft(), end="")

print(">")
