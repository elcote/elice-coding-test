# 소수&팰린드롬

```python
import sys
import math

def input(): return sys.stdin.readline().rstrip()


def is_palindrome(text: str) -> bool:
    # 문자열 중간까지만 검사하면 됨
    text_len = len(text)
    mid = text_len//2

    for i in range(mid):
        # 반대쪽 대응 하는 문자와 검사 다르면? 팰린드롬 아님 False
        if text[i] is not text[text_len-i-1]:
            return False
    return True

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

# n값의 범위는 1,000,000 이지만 그 범위 안에서 팰린드롬과 소수 조건을 만족하는 수를 못찾을 경우
# 1003001 을 반환하기 위해 여유값을 줌
maximum = 1003002

n = int(input())
for i in range(n, maximum):
    if is_prime(i) and is_palindrome(str(i)):
        print(i)
        break
```
