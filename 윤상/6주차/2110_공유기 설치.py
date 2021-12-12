import sys

def input():
    return sys.stdin.readline().rstrip()

N, R = map(int, input().split())
houses = []

for _ in range(N):
    houses.append(int(input()))
houses.sort()
# print(houses)
start = 1
end = houses[-1] - houses[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cur = houses[0]
    cnt = 1

    for i in range(1, len(houses)):
        if houses[i] >= cur + mid:
            cnt += 1
            cur = houses[i]
    if cnt >= R:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
