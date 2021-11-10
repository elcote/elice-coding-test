import sys

def input():
    return sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    N = int(input())
    Tree = [[] for _ in range(N+1)]
    for edge in range(N-1):
        parent, child = map(int, input().split())
        # Tree[parent].append(child)
        Tree[child].append(parent)
    # print(Tree)
    node1, node2 = map(int, input().split())
    
    parentsOfNode1 = [node1]
    parentsOfNode2 = [node2]
    # flag = False
    while Tree[node1] != []:
        parentsOfNode1.extend(Tree[node1])
        node1 = Tree[node1][0]
    while Tree[node2] != []:
        parentsOfNode2.extend(Tree[node2])
        node2 = Tree[node2][0]
    # print("PARENTS OF NODE1",parentsOfNode1)
    # print("PARENTS OF NODE2",parentsOfNode2)
    for item in parentsOfNode1:
        if item in parentsOfNode2:
            # flag = True
            print(item)
            break

