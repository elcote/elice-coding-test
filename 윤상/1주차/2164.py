from collections import deque

N = int(input())

ans = deque([i for i in range(1,N+1)])

while len(ans) != 1:
    ans.popleft()
    ans.append(ans.popleft())
print(*ans)