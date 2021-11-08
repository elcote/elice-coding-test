import sys
from itertools import combinations

def input():
  return sys.stdin.readline().rstrip()

def gcd(a,b):
  while b != 0:
    a, b = b, a%b
  return a

arr = []

n = int(input())

for i in range(n):
  a = list(map(int, input().split()))
  total = 0
  o =  a[0] 
  del a[0]

  comb = list(combinations(a, 2))

  for c in comb:
    g = gcd(c[0], c[1])
    total += g
  
  arr.append(total)

for e in arr:
  print(e)