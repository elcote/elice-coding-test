import sys

def input():
    return sys.stdin.readline().rstrip()

N , K = map(int, input().split())

ans = []

for i in range(2,N+1):
    ans.append(i)

count = 0
flag = False

while ans:
    for item in ans:
        P = ans[0]
        for multiples in ans:
            if multiples % P == 0:
                count += 1
                if count == K:
                    print(multiples)
                    flag = True
                    break
                ans.remove(multiples)
        if flag == True:
            break
    if flag == True:
        break    