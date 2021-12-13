#pypy3로 실행
n, m = map(int, input().split())

t = [0] * n
for i in range(n):
    t[i] = int(input())

answer = 0
start = min(t)
end = max(t) * m
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for time in t:
        tmp += mid // time
    
    if tmp >= m: #심사를 끝낸 총 인원이 m보다 크면 걸리는 시간을 줄인다.
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)





#시간초과
# t.sort()
# now = 1
# while m > 0:
#     for time in t:
#         if now % time == 0:
#             m -= 1
#     now += 1
# print(now - 1)
