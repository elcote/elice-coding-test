import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dq = deque()
ans=[]
for i in range(N):
    command = input().split()
    if command[0] == "push_front":
        dq.appendleft(str(command[1]))
    if command[0] == "push_back":
        dq.append(str(command[1]))
    if command[0] == "pop_front":
        if len(dq) == 0:
            ans.append("-1\n")
        else:
            ans.append(dq.popleft()+"\n")
    if command[0] == "pop_back":
        if len(dq) == 0:
            ans.append("-1\n")
        else:
            ans.append(dq.pop()+"\n")
    if command[0] == "size":
        ans.append(str(len(dq))+"\n")
    if command[0] == "empty":
        if len(dq) == 0:
            ans.append("1\n")
        else:
            ans.append("0\n")
    if command[0] == "front":
        if len(dq) == 0:
            ans.append("-1\n")
        else:
            ans.append(dq[0]+"\n")
    if command[0] == "back":
        if len(dq) == 0:
            ans.append("-1\n")
        else:
            ans.append(dq[-1]+"\n")
print("".join(ans))