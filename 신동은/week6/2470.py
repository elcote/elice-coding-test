#0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다.
n = int(input())
y = list(map(int, input().split()))

y.sort()
ans = 99999999999
answer = []
start = 0
end = n - 1

while start < end:
    tmp = y[end] + y[start]
    if abs(0 - tmp) < abs(0 - ans):
        ans = tmp
        answer = [y[start], y[end]]
    if tmp < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])
