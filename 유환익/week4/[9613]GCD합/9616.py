import sys
from itertools import combinations

def input():
  return sys.stdin.readline().rstrip()

# 최대 공약수를 구하는 함수 (유클리드 호제법)
def gcd(a,b):
  while b != 0:
    a, b = b, a%b
  return a

# 최대공약수의 합을 저장하는 리스트
arr = []

n = int(input())

# n만큼 순회하면서
for i in range(n):

  # 명령단을 입력 받는다
  a = list(map(int, input().split()))

  #  전체합 저장 변수, 1차 반복 시 초기화
  total = 0

  # o는 각 단의 숫자 수 
  o =  a[0] 
  
  # 숫자 수 제외
  del a[0]

  # 각 쌍의 조합을 구한다.
  comb = list(combinations(a, 2))

  # 각 조합을 순회
  for c in comb:

    # 각 쌍의 최대공약수
    g = gcd(c[0], c[1])

    # 누적
    total += g
  
  # 리스트에 전체합 넣기
  arr.append(total)

# 순회하면서 각 합 출력
for e in arr:
  print(e)