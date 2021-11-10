import sys

def input():
    return sys.stdin.readline().rstrip()

def GCD(a,b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)

n = int(input())
for _ in range(n):
    a , b = map(int,input().split())
    LCM = a*b/GCD(a,b)
    print(int(LCM))