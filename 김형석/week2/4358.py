'''
    문제 이름 : 생태학
    문제 번호 : 4358
    문제 링크 : https://www.acmicpc.net/problem/4358
'''

import sys
from collections import defaultdict

read = sys.stdin.readline
# defaultdict 사용 : 키가 존재하지 않으면 자동으로 0 입력
treeDic = defaultdict(int)
n = 0

while True:
    tree = read().rstrip()
    # 종료 조건
    if not tree:
        break
    treeDic[tree] += 1
    n += 1  # 총 나무 그루

# value를 기준으로 정렬
# item[1] = value
sortTree = sorted(treeDic.items())
for key, value in sortTree:
    # round : 소수점 반올림
    percentage = round((value/n)*100, 4)
    print(key, '%.4f' % percentage)  # 오답 이유 : '%.4f'
