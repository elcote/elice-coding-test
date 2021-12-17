'''
    문제 이름 : 단어 뒤집기2
    문제 번호 : 17413
    문제 링크 : https://www.acmicpc.net/problem/17413
'''

'''
    1. 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
    2. 문자열의 시작과 끝은 공백이 아니다.
    3. '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
'''
import sys
read = sys.stdin.readline

s = read().rstrip()
flag = False  # 태그인지 아닌지 판별
answer = ""
word = ""  # 뒤집어야 하는 단어
for i in s:
    if flag == False:
        # 태그가 아닐 경우
        if i == "<":
            # i가 여는 태그일 경우
            flag = True
            # 입력된 단어들 저장
            answer += word[::-1]  # 단어 뒤집어서 answer에 더함
            answer += i           # 여는 태그 answer에 더함
            word = ""  # 초기화
        elif i.isalnum():
            # i가 숫자 또는 알파벳일경우
            word += i
        else:
            # 공백일 경우
            answer += word[::-1]    # 단어 뒤집어서 answer에 더함
            word = ""               # 초기화
            answer += i             # 공백 더해줌
    else:
        # 태그일 경우
        answer += i
        if i == ">":
            flag = False

if word != "":
    answer += word[::-1]

print(answer)
