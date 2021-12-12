'''
    문제 이름 : 나무 자르기
    문제 번호 : 2805
    문제 링크 : https://www.acmicpc.net/problem/2805
'''

'''
이분 탐색을 진행해서 , 이분 탐색을 모두 마쳤을때 end가 벌목 높이 (정답)이되는 문제
'''

import sys
from collections import Counter
read = sys.stdin.readline

n, m = map(int, read().split())
trees = Counter(map(int, read().split()))  # Counter 사용 안하면 시간 초과 오류남

start, end = 1, max(trees)  # 시작 높이와 끝 높이 설정

# 적절한 높이 찾는 이분탐색 진행
while start <= end:
    mid = (start+end) // 2
    log = 0  # 잘라서 가져갈 통나무

    # 일반 list로 진행했을때와 Counter의 .items() 사용시 결과가 다른 이유 ?
    for i, j in trees.items():
        # 나무의 높이가 mid값 보다 작을 경우
        if i >= mid:
            # 벌목된 나무 합
            log += (i-mid) * j

    # 벌목된 나무 합이 정답보다 크거나 같을 경우
    if log >= m:
        # 시작 값 증가
        start = mid + 1
    else:
        # 끝 값 감소
        end = mid - 11

print(end)
