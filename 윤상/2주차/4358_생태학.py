import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

countTree = defaultdict(int)
count = 0
while True:
    userInput = input()
    if not userInput:
        break
    countTree[userInput] += 1
    count += 1

treeList = list(countTree.keys())
treeList.sort()
for tree in treeList:
    print(tree, '%.4f' %(countTree[tree]/count*100))