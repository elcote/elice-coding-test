import sys
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
childTree = [[]for _ in range(N)]
nodes = list(map(int,input().split()))
for i in range(len(nodes)):
    if nodes[i] == -1:
        root = i
    else:
        childTree[nodes[i]].append(i)
target = int(input())

def deleteNodes(index):
    if not childTree[index]:
        return
    else:
        for ind in childTree[index]:
            deleteNodes(ind)
    childTree[index].clear()
deleteNodes(target)
count = 0
for nodes in childTree:
    for node in nodes:
        if not childTree[node] and node != target:
            count += 1
        if len(childTree[node]) == 1 and childTree[node][0] == target:
            count += 1
if len(childTree[root]) == 1 and childTree[root][0] == target:
    count += 1
print(count)