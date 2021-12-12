import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
inspect_time = []

for _ in range(N):
    inspect_time.append(int(input()))
inspect_time.sort()
# print(inspect_time)

start = 0
# end = len(inspect_time) - 1
end = M * inspect_time[-1]
# print(inspect_time)

while start <= end:
    # print(start, end, '##')
    mid = (start + end) // 2
    total_ppl = 0
    for inspect in inspect_time:
        total_ppl += mid // inspect
    # print(total_ppl)
    # break
    if total_ppl < M:
        start = mid +1
    else:
        end = mid - 1
    # print(start,end)
print(start)