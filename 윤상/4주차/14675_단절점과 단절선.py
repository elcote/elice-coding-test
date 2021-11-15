import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

numberOfTestCase = int(input())
for _ in range(numberOfTestCase):
    command, target = map(int, input().split())

    if command == 1:
        if len(graph[target]) == 1:
            print('no')
        else:
            print('yes')
    if command == 2:
        print('yes')