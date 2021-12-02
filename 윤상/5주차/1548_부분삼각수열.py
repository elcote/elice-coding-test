import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

nums = list(map(int, input().split()))

def checkIfTriangular(arr):
    if len(arr) <= 2:
        return True
    else:
        tmpArr = combinations(arr, 3)
        for test in tmpArr:
            first = test[0]
            second = test[1]
            third = test[2]
            if first + second > third and first + third > second and second + third > first:
                continue
            else:
                return False
        return True

nums.sort()
gloCnt = 0
for i in range(len(nums)):
    triList = []
    numsVisited = [False for _ in range(N)]
    cnt = 0
    triList.append(nums[i])
    numsVisited[i] = True
    cnt += 1
    for j in range(i,len(nums)):
        if numsVisited[j] == False and j <= len(nums) - 1:
            triList.append(nums[j])
            numsVisited[j] = True
        if checkIfTriangular(triList):
            cnt += 1
        else:
            flag = False
            break
    if gloCnt < cnt:
        gloCnt = cnt
print(gloCnt-1)

    