import sys

input = sys.stdin.readline
max = -1
n = int(input())
for i in range(n):
  a, b= map(int, input().split())
  bigger = a if a >= b else b
  for i in range(1, bigger+1):
    if a % i == 0 and b % i == 0:
      max = i
  print((a*b)//max)