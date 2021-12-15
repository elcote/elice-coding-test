import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
liqs = list(map(int, input().split()))
liqs.sort()

start = 0
end = len(liqs) - 1

ans = liqs[start] + liqs[end]
al = start
ar = end

while start < end:
    
    target = liqs[start] + liqs[end]
    if abs(target) < abs(ans):
        al = start
        ar = end
        ans = target
        if ans == 0:
            break
    if target < 0:
        start += 1
    else:
        end -= 1
print(liqs[al], liqs[ar])