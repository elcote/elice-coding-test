import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
ans = 0

left, right = 0, max(arr)

while left <= right:
    mid = (left + right) // 2
    now = 0
    for cost in arr:
        if cost <= mid:
            now += cost
        else:
            now += mid

    if now <= m:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)
