# 에라토스테네스의 체

```python
import sys


def input(): return sys.stdin.readline().rstrip()


def solve(n, k):
    arr = [True for _ in range(n+1)]
    idx = 0

    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if arr[j]:
                arr[j] = False
                idx += 1
                if idx == k:
                    return j
    return -1


n, k = map(int, input().split())

print(solve(n, k))
```
