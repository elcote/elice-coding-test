import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
tastes = []

for _ in range(N):
    sour, bitter = map(int, input().split())
    tastes.append((sour, bitter))

ans = 1_000_000_000

for i in range(1,N+1):
    cases = combinations(tastes,i)
    for case in cases:
        # print(case)
        total_s = 1
        total_b = 0
        for s , b in case:
            total_s *= s
            total_b += b
        ans = min(abs(total_s - total_b), ans)
print(ans)
            
