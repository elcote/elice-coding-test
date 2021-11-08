'''
    문제 이름 : 에라토스테네스의 체
    문제 번호 : 2960
    문제 링크 : https://www.acmicpc.net/problem/2960
'''
import sys

read = sys.stdin.readline

n, m = map(int, read().split())

# 0,1은 미포함이므로 n+1개까지 생성
nums = [True] * (n+1)
cnt = 0  # m번째 숫자인지 판별할 변수

# 이중 for문을 사용하여 nums[j]의 값을 True 에서 False로
# 변경하는 식으로 소수의 배수들을 지워나간다
for i in range(2, len(nums)+1):
    # i씩 늘리는 경우
    for j in range(i, n+1, i):
        # (True = 소수) 발견시
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            # m번째 숫자를 찾은 경우
            if cnt == m and nums[j] == False:
                print(j)
                break
