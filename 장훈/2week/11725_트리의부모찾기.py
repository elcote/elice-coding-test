import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
#반복제한이 기본적으로 1000이기 때문에 늘려줘야한다 
N=int(input())#노드의 개수
Tree=[[] for _ in range(N+1)]
#트리
Parents=[0 for _ in range(N+1)]
#부모노드를 저장할 리스트

for _ in range(N-1):#노드끼리 서로 연결시켜준다
    a, b=map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i]==0:#해당노드에 부모가 없다면 시작노드가 부모노드이다
            parents[i]=start
            DFS(i, tree, parents)
DFS(1, Tree, Parents)

for i in range(2, N+1):#부모노드번호를 2번노드부터 출력
    print(Parents[i])