n = int(input())
request = list(map(int, input().split()))
m = int(input())

start = 0
end = max(request)
    
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for money in request:
        if money > mid:
            tmp += mid
        else:
            tmp += money
    if tmp <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
