import sys
N = int(input())
paren = []

for i in range(N):
    read = sys.stdin.readline().rstrip()
    paren.append(read)
    # print(len(read))
for i in range(N):
    flag = 'YES'
    count = 0
    for j in paren[i]:
        if len(paren[i])%2 != 0:
            flag = 'NO'
            break
        if j == '(':
            count += 1 
        else:
            count -= 1
        if count < 0:
            flag = 'NO'
            break
    if count > 0:
        flag = 'NO'
    print(flag)
