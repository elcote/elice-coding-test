def solution(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리
        print(f'start는 : {start}, tree[start]는 : {tree[start]} 입니다.')
        print(f'i는 : {i}, tree[i]는 : {tree[i]} 입니다.')
        print()

        if tree[start] < tree[i]: # tree[0] < tree[1]
            div = i
            break

    solution(start + 1, div - 1) # 분할 왼쪽
    solution(div, end)           # 분할 오른쪽
    
    print(f'후위순회 tree[start]는 : {tree[start]} 입니다.')
    # print(tree[start])


import sys
sys.setrecursionlimit(10 ** 9)  # 최대 재귀 깊이를 높여주기 위함 파이썬의 기본 재귀 깊이는 1000 이다.

tree = []
count = 0
# 0. 값 입력
while count <= 10000:

    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    print(f'현재 tree는 : {tree} 입니다.')
    count += 1
    print(f'현재 count는 : {count} 입니다.')

# 1. 시작
solution(0, len(tree) - 1)
