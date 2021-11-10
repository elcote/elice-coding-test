import sys
import heapq as hq
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    maxheap = []
    minheap = []
    countDict = defaultdict(int)
    T = int(input())
    for i in range(T):
        command, number = input().split()
        if command == "I":
            countDict[int(number)] += 1
            hq.heappush(minheap,int(number))
            hq.heappush(maxheap,-int(number))
        else:
            if len(minheap) == 0 or len(maxheap) == 0:
                continue
            else:
                if number == "1":
                    temp = -hq.heappop(maxheap)
                    countDict[temp] -= 1
                else:
                    temp = hq.heappop(minheap)
                    countDict[temp] -= 1
        while minheap and countDict[minheap[0]] == 0:
            hq.heappop(minheap)
        while maxheap and countDict[-maxheap[0]] == 0:
            hq.heappop(maxheap)
    if len(maxheap) == 0 or len(minheap)== 0:
        print("EMPTY")
    else:
        print(-maxheap[0], minheap[0])