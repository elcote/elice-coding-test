inputS = [w for w in input()]
ans = ''
tmp = ''
flag = False
for s in inputS:
    # print(s,ans)
    if flag:
        ans += s
        if s == '>':
            flag = False
        continue
    if s == '<':
        if len(tmp) > 0:
            ans += tmp
            tmp = ''
        ans += s
        flag = True
        continue
    
    if s == ' ':
        ans += tmp + s
        tmp = ''
        continue
    tmp = s + tmp

if len(tmp) > 0:
    ans += tmp
print(ans)
