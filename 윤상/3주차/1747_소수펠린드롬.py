import sys
import math

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
MAXIMUM = 2000000

def checkPrime(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

for i in range(N,MAXIMUM):
    if checkPrime(i):
        number = str(i)
        if number == number[::-1]:
            print(i)
            break