import sys

def input():
  return sys.stdin.readline().rstrip()

def gcd(a, b):
  while(b!=0):
    a, b = b, a%b
  return a

def lcm(a,b):
  return a*b//gcd(a,b)

n = int(input())

arr = []

for i in range(n):
  a,b = map(int, input().split())
  arr.append(lcm(a,b))

for i in range(n):
  print(arr[i])
