'''
    문제 이름 : A와B 2
    문제 번호 : 12919
    문제 링크 : https://www.acmicpc.net/problem/12919
'''

import sys
read = sys.stdin.readline;

'''
s -> t 되는 경우
1. A...A  => 1번 연산 실행시 가능
2. A...B  => 불가능..
3. B...B  => 2번 연산 실행시 가능
4. B...A => 1또는 2번 연산으로 가능
'''

#DFS , BackTracking
def translate(target):
    if len(target) == len(s):
        if target == s:
            print(1)
            exit(0) #종료
        return
    if target[0] == 'B':
        target = target[::-1]
        target.pop()
        translate(target)

        #백트래킹 위한 초기화
        target.append('B')
        target = target[::-1]

    if target[-1] == 'A':    
        target.pop()
        translate(target)

        #백트래킹 위한 초기화
        target.append('A')

s,t = [list(read().rstrip()) for _ in range(2)]


translate(t)
print(0)