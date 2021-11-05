"""
    문제 이름: LCM
    문제 번호: 5347
    문제 링크: https://www.acmicpc.net/problem/5347
    난이도: Silver IV
    태그: 유클리드 호제법, 수학, 정수론
"""
import sys

def input(): return sys.stdin.readline().rstrip()


def LCM(a, b):
    def GCD(a, b):
        while b:
            a, b = b, a % b
        return a
    return int(a * b / GCD(a, b))


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))