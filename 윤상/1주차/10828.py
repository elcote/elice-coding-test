import sys

N = int(input())
class stack:
    def __init__(self):
        self.myStack = []
    def push(self, value):
        self.myStack.append(value)
    def pop(self):
        if len(self.myStack) == 0:
            return -1
        topValue = self.myStack[-1]
        del self.myStack[-1]
        return topValue
    def top(self):
        if len(self.myStack) == 0:
            return -1
        else:
            return self.myStack[-1]
    def size(self):
        return len(self.myStack)
    def empty(self):
        if len(self.myStack) > 0:
            return 0
        else:
            return 1

s = stack()
userInput = []
for i in range(N):
    read = sys.stdin.readline().split()
    userInput.append(read)
for j in range(len(userInput)):
    if userInput[j][0] == 'push':
        s.push(int(userInput[j][1]))
    if userInput[j][0] == 'top':
        print(s.top())
    if userInput[j][0] == 'pop':
        print(s.pop())
    if userInput[j][0] == 'size':
        print(s.size())
    if userInput[j][0] == 'empty':
        print(s.empty())
