'''
    문제 이름 : 소수 & 팰린드롬
    문제 번호 : 1747
    문제 링크 : https://www.acmicpc.net/problem/1747
'''


import sys,math;
read = sys.stdin.readline;

#소수인지 아닌지 판별 (True,false)
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

#펠린드롭인지 판별
def isPalindrome(x):
    x = str(x);
    tmp = x[::-1]
    if x == tmp:
        return True
    else:
        return False;

n = int(read())
Max = 1000001 #최대값 : 1000000
answer = 0;
for i in range(n,Max):      
    #1인 경우는 제외
    if i == 1:
        continue
    #소수인 경우
    if isPalindrome(i):    #펠린드롬인 경우
        if isPrime(i):     #소수인 경우
            answer = i;
            break;

if answer == 0:
    answer = 1003001

print(answer);