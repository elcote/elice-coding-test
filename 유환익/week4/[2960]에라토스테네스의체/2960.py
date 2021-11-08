import sys

# 소수 판별 함수
def is_prime(n):
  # n이 0이거나 1인 경우 바로 함수 종료
  if n == 0 or  n == 1:
    return False

  # 2부터 n까지의 수를 자기자신과 약수가 있는 수를 제외한다.
  for i in range(2, n+1):
    if  n%i == 0:
      return False
    
    else:
      return True

def input():
  return sys.stdin.readline().rstrip()

n,k = map(int, input().split())

arr = []
cnt = 0

for i in range(2, n+1):
  if not is_prime(i):
    cnt += 1
    arr.append(i)

print(arr)
print(cnt)
print(arr[cnt-1])

