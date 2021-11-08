
"""
    문제 이름: 에라토스테네스의 체
    문제 번호: 2960
    문제 링크: https://www.acmicpc.net/problem/2960
    난이도: Silver IV
    태그: 구현, 수학, 정수론, 소수 판정, 에라토스테네스의 체
"""
import sys


def input(): return sys.stdin.readline().rstrip()


def solve(n, k):
    arr = [True for _ in range(n+1)]
    idx = 0

    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if arr[j]: 
                arr[j] = False
                idx += 1
                if idx == k:
                    return j
    return -1


n, k = map(int, input().split())

print(solve(n, k))
