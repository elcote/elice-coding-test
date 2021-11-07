import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [True] * (n+1)
# nums[0], nums[1] = False, False
cnt = 0

for i in range(2, len(nums)):
  for j in range(i, len(nums), i):
    if nums[j] == True:
      cnt = cnt + 1
      nums[j] = False
      if cnt == k:
        print(j)
        break
