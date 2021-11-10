from collections import deque
import sys
#유저 인풋 받기
N,K = map(int,sys.stdin.readline().rstrip().split())

#데큐 선언
res = deque()
ans = []

for i in range(1,N+1):
    res.append(i)
while len(res):
    res.rotate(-K)
    ans.append(res.pop())

print("<",", ".join(map(str,ans)),">",sep="")