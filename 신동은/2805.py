#PyPy3으로 실해해야 통과
n,m = map(int, input().split())
trees = list(map(int, input().split()))
minTree = 1
maxTree = max(trees)

while minTree <= maxTree:
    tmp = 0
    mid = (minTree + maxTree) // 2
    for tree in trees:
        if tree - mid > 0:
            tmp +=  tree - mid

    if tmp >= m:
        minTree = mid + 1
    else:
        maxTree = mid - 1
print(maxTree)