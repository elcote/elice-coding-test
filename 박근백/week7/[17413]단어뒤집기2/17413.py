import sys
input = sys.stdin.readline
import re

string = input().strip()
split_s = re.split("(<[^>]+>|[ ])", string)
for i in range(len(split_s)):
    if split_s[i] and split_s[i][0] != '<':
        split_s[i] = split_s[i][::-1]

print("".join(split_s))
