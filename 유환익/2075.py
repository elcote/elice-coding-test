import sys
import heapq

def input():
  return sys.stdin.readline().rstrip()


n = int(input())

lis = []

for i in range(n):
  a  = list(map(int, input().split(' ')))
  for j in a:
    heapq.heappush(lis , j)
  

  while(len(lis)> n):
    heapq.heappop(lis)

print(heapq.heappop(lis))