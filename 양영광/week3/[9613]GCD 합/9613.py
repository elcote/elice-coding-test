
"""
    문제 이름: GCD 합
    문제 번호: 9613
    문제 링크: https://www.acmicpc.net/problem/9613
    난이도: Silver III
    태그: 유클리드 호제법, 수학, 정수론
"""
import sys

def input(): return sys.stdin.readline().rstrip()

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(int(input())):

    nums = list(map(int, input().split()[1:]))

    nums_count = len(nums)

    answer = 0

    # combination
    for i in range(nums_count):
        for j in range(i+1, nums_count):
            answer += GCD(nums[i], nums[j])

    print(answer)