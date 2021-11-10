import sys
from collections import deque

N = int(input())
class queue:
    def __init__(self):
        self.myQueue = deque()
    def push(self, value):
        self.myQueue.append(value)
    def pop(self):
        if len(self.myQueue) == 0:
            return -1
        return self.myQueue.popleft()
    def size(self):
        return len(self.myQueue)
    def empty(self):
        if len(self.myQueue) > 0:
            return 0
        else:
            return 1
    def front(self):
        if len(self.myQueue) == 0:
            return -1
        else:
            return self.myQueue[0]
    def back(self):
        if len(self.myQueue) == 0:
            return -1
        else:
            return self.myQueue[-1]

s = queue()
ans = []
for i in range(N):
    userInput = sys.stdin.readline().rstrip().split()
    if userInput[0] == 'push':
        s.push(int(userInput[1]))
    if userInput[0] == 'pop':
        ans.append(s.pop())
    if userInput[0] == 'size':
        ans.append(s.size())
    if userInput[0] == 'empty':
        ans.append(s.empty())
    if userInput[0] == 'front':
        ans.append(s.front())
    if userInput[0] == 'back':
        ans.append(s.back())
for c in ans:
    print(c)