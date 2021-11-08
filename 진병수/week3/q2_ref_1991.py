'''

preorder 전위순회 과정입니다.

입력값
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

'''

import sys

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):    # 전위순회
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right

preorder('A')