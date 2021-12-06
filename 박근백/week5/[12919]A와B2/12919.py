import sys
input = sys.stdin.readline

def recur(depth, val, check):
    global ck
    if depth >= len(t):
        if check:
            if val == reversed_t:
                ck = 1
        else:
            if val == t:
                ck = 1
        return

    if ck:
        return

    if val not in t and val not in reversed_t:
        return

    if check:
        recur(depth + 1, 'A' + val, check)
    else:
        recur(depth + 1, val + 'A', check)

    if check:
        recur(depth + 1, "B" + val, False)
    else:
        recur(depth + 1, val + 'B', True)

s = input().strip()
t = input().strip()
reversed_t = t[::-1]
ck = 0

recur(len(s), s, False)
print(ck)
