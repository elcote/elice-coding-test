####################################################
'''
< LCM 최소공배수 >
두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오.
'''
####################################################
'''
< 최대 공약수 구하기 >
for i in range(min(a,b), 0, -1):
    if a%i == 0 and b%i == 0:
        print(i)
        break

# 최대 공약수 구하기 설명 #
a,b 중 작은 숫자부터 1까지 -1을 하며 for문을 실행시킵니다.
만약 a%i, b%i 값이 모두 딱 떨어져 나머지가 없는 상태라면
이때 사용된 i 는 a와 b의 최대공약수입니다.
찾은 순간 break로 빠져나옵니다.

'''
####################################################
'''
< 최소 공배수 구하기 >
for i in range(max(a,b), (a*b)+1):
    if i%a == 0 and i%b == 0:
        print(i)
        break

# 최소 공배수 구하기 설명 #
a,b중 더 큰 숫자부터 a*b의 수까지 for문을 실행시킵니다.
더 큰 숫자부터 실행하는 이유는 a,b의 배수들 중 공통부분을 찾는 것이기 때문에
a,b중 작은 수부터 시작하게되면 i가 ++1이 되면서 둘 중 큰 수에 도달할 때까지 for문은 헛돌게 됩니다.

i%a, i%b == 0 모두 값이 떨어지는 나머지가 없는 상태라면 이 때 사용된 i는 a와 b의 최소공배수 입니다.

최소 공배수는 공통 배수들 중 가장 작은 것을 구하는 것이므로 for 문을 주어진 수 부터 +1을 했습니다.
어디서부터 시작하는건 상관없지만 최대한 빨리 찾아서 for문을 끝내는게 효율이 좋기 때문입니다.

'''
####################################################
'''
<유클리드 호제법>

'유클리드 호제법' 으로 최대공약수와 최소공배수를 간단하게 구할 수 있습니다.

x, y 의 최대공약수는 y, r 의 최대공약수와 같다는 원리를 이용하는 것입니다.

(r == x 를 y 로 나눈 나머지값)

(x 와 y 최대공약수 == y 와 r 의 최대공약수) 

즉 계속해서 x 에는 y 값을 대입하고 y 에는 (x % y) 값인 r을 대입하다보면

언젠가는 x % y == 0 일 때가 있습니다.

# 유클리드 호제법을 이용한 파이썬 알고리즘

# 최대공약수 구하기
def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

print(GCD(10, 12))  # 2

# 최소공배수 구하기
def LCM(x, y):
    result = (x*y) // GCD(x, y)
    return result

print(LCM(10,12))    # 60


'''
####################################################
''' # 시간초과

import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())    
    for i in range(max(a,b), (a*b)+1):
        if i%a == 0 and i%b == 0:
            print(i)
            break

'''
####################################################

import sys
input = sys.stdin.readline

def gcd(x, y):          # 유클리드 호제법을 이용한 GCD (최대 공약수) 구하기
    while y:
        x, y = y, x%y
    return x

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())    # x * y 를 최대공약수로 나눈 몫이 LCM (최소 공배수) 이다.
    print(a*b//gcd(a, b))

####################################################