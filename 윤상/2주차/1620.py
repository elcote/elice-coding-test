import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())
DD = defaultdict()

ans = []
for i in range(N):
    DD[i+1] = input()

reverse = dict(map(reversed, DD.items()))

for i in range(K):
    userInput = input()
    if userInput.isdigit():
       ans.append(DD[int(userInput)])
    else:
        ans.append(reverse[userInput])
for c in ans:
    print(c)