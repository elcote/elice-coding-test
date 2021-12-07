#이진검색트리
import sys

sys.setrecursionlimit(10**9)
preorder=[]

while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
postorder=[]

def postorderset(preorder, left, right):
    if left>right:
        return
    root=preorder[left]
    ls=left+1
    re=right
    rs=right+1
    for i in range(right-left+1):
        if i==0:
            continue
        if preorder[left+i]>root:
            rs=i+left
            break
    le=rs-1
    postorderset(preorder, ls, le)
    postorderset(preorder, rs, re)
    postorder.append(root)

postorderset(preorder, 0, len(preorder)-1)

for i in postorder:
    print(i)