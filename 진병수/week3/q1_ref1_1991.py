'''
inorder 중위순회 과정입니다.
'''

''' 

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
    print(tree)

def inorder(root):
    print(f'현재 root {root}')
    if root != '.':
        inorder(tree[root][0])  # left
        print(f'현재 root 는 {root} 입니다.', end='\n')     # root
        inorder(tree[root][1])  # right

inorder('A')