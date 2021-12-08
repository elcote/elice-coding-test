'''
    문제 이름 : 바이러스
    문제 번호 : 2606
    문제 링크 : https://www.acmicpc.net/problem/2606
'''

import sys
read = sys.stdin.readline

dic = {}
visited = []


# 깊이 탐색
def DFS(start, dic):
    for i in dic[start]:
        if i not in visited:  # 방문 하지 않았을경우
            visited.append(i)  # visited 배열에 추가
            DFS(i, dic)  # 타고 들어가서 다시 탐색


for i in range(int(read())):
    dic[i+1] = set()  # 컴퓨터의 개수
for j in range(int(read())):
    a, b = map(int, read().split())
    # 서로 연결되어있는것이기 때문에 둘다 더해줌
    dic[a].add(b)
    dic[b].add(a)

DFS(1, dic)
print(len(visited)-1)
