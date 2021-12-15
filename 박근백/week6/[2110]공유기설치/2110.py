import sys
input = sys.stdin.readline

n, c = map(int, input().split())
pos = []
ans = 0

for _ in range(n):
    pos.append(int(input()))

pos.sort()

left = 0
right = pos[-1]

while left <= right:
    mid = (left + right) // 2
    count = 1
    dist = mid
    for i in range(1, len(pos)):
        dist -= pos[i] - pos[i - 1]
        if dist <= 0:
            dist = mid
            count += 1
    if count >= c:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)





