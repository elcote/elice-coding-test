'''
<단어 뒤집기 2>

- 문제 -
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.

'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고, '<'와 '>' 사이에는 알파벳 소문자와 공백만 있다.

단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다. 
태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

- 입력 -
첫째 줄에 문자열 S가 주어진다. S의 길이는 100,000 이하이다.

- 출력 -
첫째 줄에 문자열 S의 단어를 뒤집어서 출력한다.

- 예제 입력 1 -
baekjoon online judge

- 예제 출력 1 -
noojkeab enilno egduj

- 예제 입력 2 -
<open>tag<close>

- 예제 출력 2 -
<open>gat<close>
'''

# import sys

# print(sys.builtin_module_names)

import sys

input = sys.stdin.readline

s = input().rstrip()
flag = False
word = ""
answer = ""

for i in s:
    if flag == False:
        if i == "<":            # i 가 "<" 인 경우
            flag = True         # flag 를 True 로 바꾸고
            word += i           # word 문자열에 i 를 추가

        elif i == " ":          # i 가 공백인경우
            word += i           # word 문자열에 i 를 추가
            answer += word
            # print(f"현재 answer 입니다. {answer}\n")
            word = ""
            
        else:                   # i 가 위의 어떠한 경우에도 해당하지 않으면
            word = i + word     # 거꾸로 문자를 입력해준다.
            # print(f"현재 word 입니다. {word}\n")

    elif flag == True:          # flag 가 True 인 경우
        word += i               # word 문자열에 i 를 추가
        
        if i == ">":            # i 가 ">" 인 경우
            flag = False        # flag 를 False 로 바꾸고
            answer += word      # answer 문자열에 word 를 추가
            word = ""           # word 초기화
            # print(f"현재 answer 입니다. {answer}\n")

print(answer + word)