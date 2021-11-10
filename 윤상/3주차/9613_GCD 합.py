import sys
from itertools import combinations
from math import gcd

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    numbers = list(map(int,input().split()))
    sum = 0
    numbers.pop(0)
    
    gcdsBefore = combinations(numbers,2)
    # print(list(gcdsBefore))
    for combination in gcdsBefore:
        sum += gcd(combination[0],combination[1])
    print(sum)

    