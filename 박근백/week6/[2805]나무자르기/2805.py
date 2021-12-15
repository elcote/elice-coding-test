import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def binary():
    ans = 0
    left, right = 0, 1_000_000_001
    while left <= right:
        mid = (left + right) // 2
        length = 0
        for tree in trees:
            if tree >= mid:
                length += tree - mid
        if length >= m:
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1
    return ans
print(binary())

