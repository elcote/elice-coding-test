import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
arr = []

ans = 1_000_000_001

for _ in range(n):
    s, b = map(int, input().split())
    arr.append((s, b))

for i in range(1, n + 1):
    for comb in combinations(arr, i):
        total_s = 1
        total_b = 0
        for s, b in comb:
            total_s *= s
            total_b += b
        ans = min(ans, abs(total_s - total_b))

print(ans)
