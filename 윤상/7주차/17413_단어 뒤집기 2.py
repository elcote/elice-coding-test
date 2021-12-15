import sys
import re

def input():
    return sys.stdin.readline().rstrip()

string = input()
converted = list(filter(lambda x : x, re.split(r"(<[a-z0-9 ]+>)", string)))
# print(converted)
ans = ''
for c in converted:
    if c.startswith("<"):
        ans += c
    else:
        tmp = re.split("( )",c)
        for s in tmp:
            ans += s[::-1]
print(ans)

# print(string)