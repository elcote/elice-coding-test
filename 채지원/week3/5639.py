import sys

def tree(start, end):
  if start > end:
    return
  
  d = end + 1
  for i in range(start + 1, end + 1):
    if pre[start] < pre[i]:
      d = i
      break
    
  tree(start + 1 , d - 1) #왼쪽 트리
  tree(d, end) # 오른쪽 트리
  print(pre[start])

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

pre = []
count = 0

while True:
  try:
    num = int(input())
  except:
    break
  pre.append(num)

tree(0, len(pre)-1)