import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
max_length = 0

for i in range(len(arr)):
    temp = [arr[i]]
    for j in range(i + 1, len(arr)):
        if len(temp) < 2:
            temp.append(arr[j])
            continue

        if temp[0] + temp[1] <= arr[j]:
            break
        temp.append(arr[j])

    max_length = max(max_length, len(temp))
print(max_length)
