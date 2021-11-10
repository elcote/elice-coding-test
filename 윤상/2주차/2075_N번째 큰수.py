import sys
import heapq as hq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ans = []

for i in range(N):
    lis = list(map(int,input().split()))
    if not ans:
        for item in lis:
            hq.heappush(ans,item)
    else:
        for item in lis:
            if ans[0] < item:
                hq.heappop(ans)
                hq.heappush(ans,item)
            else:
                continue
print(ans[0])