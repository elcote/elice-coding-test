# GCD 합

## 정답 코드

```python
import sys

def input(): return sys.stdin.readline().rstrip()

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(int(input())):

    # 가장 앞 원소는 생략한다.
    nums = list(map(int, input().split()[1:]))

    nums_count = len(nums)

    answer = 0

    # combination
    for i in range(nums_count):
        for j in range(i+1, nums_count):
            answer += GCD(nums[i], nums[j])

    print(answer)
```
