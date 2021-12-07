import math

def isPrime(x):#약수의 특성상 가운데값에서 대칭=> 루트를이용해 반으로 줄인다
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i ==0:
            return False
    return True

N=int(input())
result=0

for i in range(N, 1000001):
    if i==1:
        continue
    if str(i)==str(i)[::-1]:#입력값과 거꾸로돌린 값을 비교하고 소수인지판별
        if isPrime(i)==True:
            result=i
            break

if result==0:
    result=1003001
print(result)