import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

budget = list(map(int, input().split()))
total = int(input())
budget.sort()
start = 1
end = budget[-1]
# print(end)
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for bud in budget:
        tmp += bud if bud <= mid else mid
    # print(tmp)
    if tmp > total:
        end = mid - 1
    else:
        start = mid + 1
print(end)