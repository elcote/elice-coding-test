'''
<GCD 최대 공약수 합 구하기>

Greatest Common Divisor - 최대 공약수

양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있다. 
각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 
입력으로 주어지는 수는 1,000,000을 넘지 않는다.

-입력-
4 10 20 30 40

-출력-
70

# 기본적으로 최대 공약수를 어떻게 구하는지 모르겠음

# 유클리드 호제법을 알아야 풀 수 있는 문제라함 -> 유클리드 호제법에 대해서 알아보자!

<유클리드 호제법>

유클리드 호제법 공식은 다음과 같습니다.

1. 최대공약수를 구하는 함수를 gcd(x,y) 라고 가정
2. x % y == 0 이라면 gcd(x, y) = y 가 성립
3. x % y != 0 이라면 gcd(x, y) = gcd(x, x % y) 가 성립

2번이 될 때까지 2~3번 반복?

def gcd(x, y):
    # y가 0이 될 때 까지 반복
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x

print(gcd(1071, 1029))

'''

####################################################
'''
import sys
import math

input = sys.stdin.readline() # input 변수로 만들어 쓸때

n = int(input)

for i in range(n):
    arr = list(map(int, input.split()))
    total = 0
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            total += math.gcd(arr[j],arr[k])
    print(total)
'''
#####################################################

import sys
import math

n = int(input())    # input 함수로 쓸때, test 케이스 n개

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    total = 0
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            total += math.gcd(arr[j],arr[k])    # gcd 모듈 이용
    print(total)

#####################################################