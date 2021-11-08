'''
    문제 이름 : 스택
    문제 번호 : 10828
    문제 링크 : https://www.acmicpc.net/problem/10828
'''
import sys

num = int(input())
stack = []  # 스택으로 사용할 배열 생성

for i in range(num):
    command = sys.stdin.readline().split()

    # push
    if command[0] == "push":
        stack.append(command[1])
    # pop
    elif command[0] == "pop":
        # 스택 비어있는 경우
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    # size
    elif command[0] == "size":
        print(len(stack))
    # empty
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # top
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            # 제일 위 = 가장 늦게 들어간 요소
            print(stack[-1])
