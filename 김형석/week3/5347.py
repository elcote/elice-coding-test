'''
    문제 이름 : LCM
    문제 번호 : 5347
    문제 링크 : https://www.acmicpc.net/problem/5347
'''
import sys
read = sys.stdin.readline


def gcd(a, b):
    while b:
        n = b
        b = a % b
        a = n
    return int(a)


n = int(read())
for _ in range(n):
    a, b = map(int, read().split())
    print((a*b)//gcd(a, b))
