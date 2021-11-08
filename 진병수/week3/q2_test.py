
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
Q=[50, 30, 24, 5, 28, 45, 98, 52]
ans=[]

# while True:
#     try:
#         Q.append(int(input()))
#     except:
#         break

# 3. BS 정의
def BS(L,R,root):
    x=L
    if Q[R]>root:
        while L<=R:
            mid=(L+R)//2
            if Q[mid]>root:
                R=mid-1
            else:
                L=mid+1
        if Q[mid]>root:
            return mid
        else:
            return mid+1
    else:
        return x

# 2. divide
def divide(left,right):
    if left==right:
        ans.append(Q[left])
        return
    root=Q[left]
    ans.append(root)

    # 3. BS 작동
    temp=BS(left+1,right,root)
    if temp==left+1:
        divide(temp,right)
        return
    else:
        divide(temp, right)
        divide(left+1,temp-1)

# 1. 시작
divide(0,len(Q)-1)

for i in ans[::-1]:
    print(i)