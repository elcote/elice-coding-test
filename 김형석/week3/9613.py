'''
    문제 이름 : GCD 합
    문제 번호 : 9613
    문제 링크 : https://www.acmicpc.net/problem/9613
'''
import sys
from itertools import combinations;
# from itertools import product => 두개 이상의 리스트의 모든 조합

read = sys.stdin.readline;

def gcd(a,b):
    while b:
        n = b
        b = a%b
        a = n
    return int(a)

n = int(read());
sum = 0;

for _ in range(n):
    arr = list(map(int,read().split()))
    
    arr = arr[::-1]                         #테스트 케이스의 개수를 맨 뒤로 보내기 위해 역순으로 정리
    del arr[len(arr)-1]                     #마지막 요소 제거 (테스트 케이스 .. 문제 잘 읽자)
    #조합을 위한 combinations (순열은 permutations)
    ncr = combinations(arr,2)
    
    for i in ncr:
        #조합을 gcd에 넣어서 최대공약수 찾기 (math.gcd 이용해도 무방)
        sum+=gcd(i[0],i[1])
    print(sum)
    sum = 0;

'''
======삼중 for 문======
import sys

read = sys.stdin.readline;

def gcd(a,b):
    while b:
        n = b
        b = a%b
        a = n
    return int(a)

n = int(read());

for _ in range(n):
    arr = list(map(int,read().split()))
    sum = 0;
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            sum += gcd(arr[i],arr[j]);
        
    print(sum)
'''


