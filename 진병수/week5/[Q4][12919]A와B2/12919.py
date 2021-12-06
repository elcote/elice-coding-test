'''
-문제-
수빈이는 A와 B로만 이루어진 영어 단어 존재한다는 사실에 놀랐다. 
대표적인 예로 AB (Abdominal의 약자), BAA (양의 울음 소리), AA (용암의 종류), ABBA (스웨덴 팝 그룹)이 있다.

이런 사실에 놀란 수빈이는 간단한 게임을 만들기로 했다. 
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 
문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.

문자열의 뒤에 A를 추가한다.
문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오. 

-입력-
첫째 줄에 S가 둘째 줄에 T가 주어진다. 
(1 ≤ S의 길이 ≤ 49) 
(2 ≤ T의 길이 ≤ 50)
(S의 길이 < T의 길이)

-출력-
S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
'''

'''
-예제 입력1-
A
BABA

-예제 출력1-
1
'''

'''
-예제 입력2-
BAAAAABAA
BAABAAAAAB

-예제 출력2-
1
'''


# 아이디어
# S 를 T 로 고치려 하지말고
# T 를 S 로 바꾸려고 하면 된다.

# A로 끝나는 경우는 A를 뒤에서 삭제하고, 
# B로 시작하는 경우는 뒤집고 B를 뒤에서 삭제하는 방식으로 재귀함수를 구현해서 진행한다.

import sys

def input():
    return sys.stdin.readline().rstrip()

S = input()
T = input()

def check(now):
    if now == S:                    # T 가 S 와 똑같은 경우
        return 1

    elif len(now) == len(S):        # T 보다 S 길이가 같은데 다른 문자인경우
        return 0

    answer = 0                      # answer = 0 으로 초기화

    if now[-1] == 'A':              # 오른쪽 끝이 A 인 경우
        answer = check(now[:-1])    # 슬라이싱 - 가장 오른쪽 끝 A 를 버린다.
        
        if answer == 1:             # 재귀로 check 한 return 값이 1 인 경우
            return answer           # 그대로 return answer 하고 종료

    if now[0] == 'B':               # 왼쪽 끝이 B 인 경우
        temp = now[::-1]            # 앞,뒤 를 뒤집는다.
        answer = check(temp[:-1])   # 슬라이싱 - 가장 오른쪽 끝 B 를 버린다.

    return answer                   # 왼쪽 끝이 B 인 경우도 진행하고 
                                    # answer 값이 1 인경우, 0 인 경우 상관없이 일단 종료

# 시작
answer = check(T)

print(answer)