'''
    문제 이름 : 입국 심사
    문제 번호 : 3079
    문제 링크 : https://www.acmicpc.net/problem/3079
'''

'''
이분 탐색
경계깂 : 최단 검사시간 ~ 최장 검사시간 * 인원수
중간값(시간) 동안 검사할수 있는 인원수 = total
m보다 total이 더 크거나 같을경우:
    끝 값 변경
    결과로 출력할 값 변경
m보다 total이 작을경우:
    시작 값 변경
'''

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
check_time = [int(read()) for _ in range(n)]

start = min(check_time)  # 최단 검사시간
answer = end = max(check_time) * m  # 최장 검사시간 * 검사 인원수

while start <= end:
    total = 0  # mid 시간동안 검사할 수 있는 인원 수
    mid = (start+end) // 2

    for i in range(n):
        total += mid // check_time[i]

    # m보다 많은 사람을 탐색한 경우
    if total >= m:
        end = mid - 1   # 끝 값 줄임
        answer = min(answer, mid)
    else:
        # m보다 적은 사람을 탐색한 경우
        start = mid + 1

print(answer)
