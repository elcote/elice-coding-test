import sys

def input():
    return sys.stdin.readline().rstrip()

N , M = map(int, input().split())

ans = dict()
count = 0

for i in range(N):
    ans[input()]=1

for j in range(M):
    userInput = input()
    if userInput in ans:
        count += 1
print(count)