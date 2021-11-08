import sys

def input():
  return sys.stdin.readline().rstrip()

# 유클리드 호제법 사용하여 최대공약수를 구하는 함수를 구현한다
def gcd(a, b):
  
  # 인수 b 을 기준으로 나눠서 0이 되기까지
  while(b!=0):
    # a에 b의 값을 대입하고, b는 a를 b로 나눈 나머지를 대입하는 것을 반복한다.
    a, b = b, a%b
  # 반복문이 끝나면 나눈 나머지가 0이 되는 시점에서 나온 결과물 a를 리턴 => 최대공약수
  return a

# 위의 최대공약수 함수를 활용하여
def lcm(a,b):
  
  # a+b 매개변수를 곱한 값을 최대공약수로 나눈 몫을 리턴 => 최소공배수
  return a*b//gcd(a,b)

n = int(input())

arr = []

for i in range(n):
  a,b = map(int, input().split())
  
  # 배열에 각 최대 공배수를 넣어 리스트를 채운다.
  arr.append(lcm(a,b))

# 요소를 차례대로 출력.
for i in range(n):
  print(arr[i])
