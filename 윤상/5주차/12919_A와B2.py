import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

S = input()
T = input()
Q = deque()

def first(S):
    return S + 'A'
def second(S):
    return 'B' + S[::-1]

cnt = len(T)-len(S)
Q.append(S)
looping = len(Q)
flag = False

while cnt > 0:
    while looping > 0:
        cur = Q.popleft()
        s1 = first(cur)
        if s1 == T:
            flag = True
            break
        else:
            if s1 in T or s1[::-1] in T:
                Q.append(s1)
        s2 = second(cur)
        if s2 == T:
            flag = True
            break
        else:
            if s2 in T  or s2[::-1] in T:
                Q.append(s2)
        looping -= 1
    if flag == True:
        break
    looping = len(Q)
    cnt -= 1
setQ = set(Q)
if flag == True:
    print(1)
else:
    for string in list(setQ):
        if string == T:
            print(1)
            break
    else:
        print(0)
