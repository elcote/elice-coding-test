'''
    문제 이름 : 예산
    문제 번호 : 2512
    문제 링크 : https://www.acmicpc.net/problem/2512
'''

'''
1.모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
2.모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다. 
'''

import sys
read = sys.stdin.readline

n = int(read())

budgets = list(map(int, read().split()))
m = int(read())

start, end = 1, m
answer = 0

if sum(budgets) <= m:
    # 1번의 경우
    answer = max(budgets)
else:
    # 2번의 경우 (이분탐색 진행)
    while start <= end:
        mid = (start+end)//2
        # mid 보다 작으면 예산 그대로 발행 , 아니면 mid 값으로 대체해서 발행
        binary_budget = [budget if budget <=
                         mid else mid for budget in budgets]

        if sum(binary_budget) <= m:
            answer = max(answer, mid)
            start = mid+1
        else:
            end = mid - 1

print(answer)
