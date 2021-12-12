import sys

def input():
    return sys.stdin.readline().rstrip()

N , M = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()
ans = 0
start = 1
end = trees[-1]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cut_trees = [tree - mid for tree in trees if tree-mid > 0]
    curr_sum = sum(cut_trees)
    if curr_sum < M:
        end = mid - 1
    elif curr_sum >= M:
        start = mid + 1
    # elif sum(cut_trees) == M:
    #     ans = mid
print(end)
# print(start, end)
