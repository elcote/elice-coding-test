'''

<GCD 최대공약수 구하기>

'''

num1 = int(input("첫번째 수를 입력하세요 : "))
num2 = int(input("두번째 수를 입력하세요 : "))

for i in range(1, num1 + 1):
  if (num1 % i == 0) & (num2 % i == 0):
    gcd = i
    
    # gcd 를 1부터 가장 큰 최대 공약수까지 계속 업데이트하며 반복한다.
  
print("%d와 %d의 최대공약수는 %d"%(num1, num2, gcd))