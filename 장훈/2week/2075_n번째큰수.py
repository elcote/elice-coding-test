import sys
import heapq

N=int(input()) 



heap=[]

for _ in range(N):
    nums=list(map(int, sys.stdin.readline().split()))

    if not heap:#heap이 비어있다면
        for num in nums:
            heapq.heappush(heap, num)#heap에 첫 입력라인을push
    else:#heap에 무언가들어있다면
        for num in nums:
            if heap[0]<num:#num의 값이 현재heap에서의 최소값보다 크다면
                heapq.heappush(heap, num)#더 큰값 push
                heapq.heappop(heap)#가장 작은 값 pop
print(heap[0])
