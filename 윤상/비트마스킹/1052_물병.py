import sys
from math import sqrt
import time
def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
number = N
purchase = 0

for i in range(1,N):
    if number % 2 != 0:
        purchase += (2**(i-1))
        number = number//2 + 1
    else:
        number = number//2  
    # print("회차 ",i)
    # print("현재 물병 개수 ", number)
    # print("현재 물병하나의 리터 ", (2**(i-1)))
    # print("구입한 물병 수 ",purchase)
    # print("@@@@")
    if number == 2**K or number < 2**K:
        print(purchase)
        break
else:
    print(-1)
