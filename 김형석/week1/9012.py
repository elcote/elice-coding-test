'''
    문제 이름 : 괄호
    문제 번호 : 9012
    문제 링크 : https://www.acmicpc.net/problem/9012
'''
import sys

n = int(sys.stdin.readline())

for i in range(n):
    #문자열 받아서 brackets에 저장 (마지막 공백 제거)
    brackets = sys.stdin.readline().strip()
    Blist = list(brackets)      #리스트에 하나씩 저장
    sum = 0
    for i in Blist:
        #"(" 일 경우 총합에 + 1
        if i == "(":
            sum += 1
        #")" 일 경우 총합 -1
        elif i == ")":
            sum -= 1
        #도중에 총합이 0보다 작아지면 = 닫힌 괄호가 더 먼저 들어온 경우
        if sum < 0:
            #NO 출력 후 반복문 탈출
            print("NO")
            break
    
    #열린 괄호가 남은 경우
    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")


''' 틀린 풀이
for i in range(n):
    brackets = sys.stdin.readline().strip()
    Blist = list(brackets)
    print(Blist)
    for i in Blist:
        print(stack)
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
'''
