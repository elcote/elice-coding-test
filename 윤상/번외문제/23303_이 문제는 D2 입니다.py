import sys
def input():
    return sys.stdin.readline().rstrip()
userInput = input()
flag = False
for i in range(len(userInput)-1):
    if (userInput[i] == "D" or userInput[i] == "d") and userInput[i+1] == "2":
        print("D2")
        flag = True
if flag == False:
    print("unrated")