import sys, math

input = sys.stdin.readline
n = int(input())
for i in range(n):
  result = 0
  arr = list(map(int, input().split()))
  for i in range(1, len(arr)):
    for j in range(i + 1, len(arr)):
      result = result + math.gcd(arr[i], arr[j])
  print(result)