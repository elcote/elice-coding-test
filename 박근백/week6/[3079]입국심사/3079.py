import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = []
ans = 10**18

for _ in range(n):
    times.append(int(input()))

left, right = 0, 10**18

while left <= right:
    mid = (left + right) // 2
    count = 0
    for t in times:
        if t <= mid:
            count += mid // t
    if count >= m:
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)
