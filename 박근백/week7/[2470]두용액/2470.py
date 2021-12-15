import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = [1_000_000_000, 1_000_000_000]
now = abs(sum(ans))

for i, el in enumerate(arr):
    left = i + 1
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if abs(arr[mid] + el) < now:
            ans = [el, arr[mid]]
            now = abs(el + arr[mid])
        if arr[mid] + el < 0:
            left = mid + 1
        else:
            right = mid - 1

print(*ans)