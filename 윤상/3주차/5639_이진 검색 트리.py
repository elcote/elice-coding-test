import sys
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

preOrder = [] #입력받은 프리오더 배열

# 아무것도 안들어올때까지 계속 입력을 받음
# while True:
#     userInput = input()
#     if not userInput:
#         break
#     else:
#         preOrder.append(int(userInput))
while True:
    userInput = input()
    try:
        preOrder.append(int(userInput))
    except:
        break


postOrder = []

def getSubTrees(start, end):
    if start > end:
        return
    else:
        index = end
        for i in range(start, end+1):
            if preOrder[i] > preOrder[start]:
                index = i-1
                break
        getSubTrees(start+1,index) # left Sub Tree
        getSubTrees(index+1,end) # right Sub Tree
        postOrder.append(preOrder[start])
        

getSubTrees(0,len(preOrder)-1)

for node in postOrder:
    print(node)