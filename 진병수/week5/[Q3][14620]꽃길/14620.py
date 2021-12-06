'''
-문제-

진아가 가진 꽃의 씨앗은 꽃을 심고나면 정확히 1년후에 꽃이 피므로 진아는 다음해 식목일 부터 꽃길을 걸을 수 있다.

하지만 진아에게는 꽃의 씨앗이 세개밖에 없었으므로 세 개의 꽃이 하나도 죽지 않고 1년후에 꽃잎이 만개하길 원한다.

꽃밭은 N*N의 격자 모양이고 진아는 씨앗을 (1,1)~(N,N)의 지점 중 한곳에 심을 수 있다. 

꽃의 씨앗은 그림 (a)처럼 심어지며 1년 후 꽃이 피면 그림 (b)모양이 된다.

꽃을 심을 때는 주의할 점이있다. 

어떤 씨앗이 꽃이 핀 뒤 다른 꽃잎(혹은 꽃술)과 닿게 될 경우 두 꽃 모두 죽어버린다. 

또 화단 밖으로 꽃잎이 나가게 된다면 그 꽃은 죽어버리고 만다.



그림(c)는 세 꽃이 정상적으로 핀 모양이고 그림(d)는 두 꽃이 죽어버린 모양이다.

하이테크 앞 화단의 대여 가격은 격자의 한 점마다 다르기 때문에 

진아는 서로 다른 세 씨앗을 모두 꽃이 피게하면서 가장 싼 가격에 화단을 대여하고 싶다.

단 화단을 대여할 때는 꽃잎이 핀 모양을 기준으로 대여를 해야하므로 꽃 하나당 5평의 땅을 대여해야만 한다.

돈이 많지 않은 진아를 위하여 진아가 꽃을 심기 위해 필요한 최소비용을 구해주자!
'''

'''
-입력-
첫째 줄에 화단의 한 변의 길이 N(6≤N≤10)이 들어온다.
이후 N개의 줄에 N개씩 화단의 지점당 가격(0≤G≤200)이 주어진다.

-출력-
꽃을 심기 위한 최소 비용을 출력한다.
'''

'''
-예제 입력-
6
1 0 2 3 3 4
1 1 1 1 1 1
0 0 1 1 1 1
3 9 9 0 1 99
9 11 3 1 0 3
12 3 0 0 0 1

-예제 출력-
12
'''

# DFS를 이용한 방법은 차례대로 탐색하면 된다.

# step 1)
# 꽃을 피울 수 있는 좌표의 범위는 동일하다. (1 ~ N-1)
# 따라서 해당 범위의 행, 열 좌표에 대해 DFS 탐색을 진행한다.

# visited : 꽃을 피운 좌표를 담는 배열
# cost : 꽃을 피운 자리의 대여비용 합을 담을 변수

# step 2)
# 특정 좌표가 방문한적이 없다면 check 함수를 통해 현위치 포함, 인접한 4개의 칸에도 방문한적이 없는지 확인한다.

# 5개의 칸 모두 방문한적이 있으면 다음 좌표를 탐색하고
# 5개의 칸 모두 방문한적이 없다면 방문처리 및 대여비용을 누적시켜 진행한다.

# step 3)
# dfs의 종료조건은 3개의 꽃이 모두 피었을 때이다.
# cnt 로 꽃이 핀 갯수를 카운트 해주었으므로 cnt 가 3이 되면 dfs 를 종료한다.
# 참고, 시간 단축을 위해 dfs 진행 중 대여비용(cost)의 누적이 최소 비용(answer)보다 같거나 크면 종료하게끔 하는 방법도 있다. -> greedy 기법?

import sys

def input():
    return sys.stdin.readline().rstrip()

flower_dir = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]                  # 현위치 상, 하, 좌, 우

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = 3001                                                       # cost의 최댓값은 200 x 5 x 3 = 3000 
                                                                    # 3001 보다 클 수 없음. 

def check(y,x):
    global n
    for dy, dx in flower_dir:                                       # 현위치, 상,하,좌,우 모두 방문 표시 
        ny = dy + y
        nx = dx + x
        if 0>ny or ny>n-1 or 0>nx or nx>n-1 or visited[ny][nx]:     # 범위를 벗어나건, 이미 방문햇다면
            return False                                            # False    
    return True                                                     # 그렇지 않다면 True

def calculate(y,x):                 # 현위치에서
    global n    
    result = 0
    for dy, dx in flower_dir:       # 현위치, 상, 하, 좌, 우
        ny = dy + y
        nx = dx + x
        result += graph[ny][nx]     # 현위치, 상, 하, 좌, 우 cost 를 result 에 더한다.
    return result

# 3개 꽃 고르기
# 서로 겹치지 않게 하기
# 오른쪽 끝까지 갔으면 다음 줄로 넘어갈 수 있도록 하기

def dfs(x, cost, cnt):
    global answer
    if cnt == 3:                                        # 꽃의 갯수 cnt 가 3이면 종료 (탈출 조건)
        answer = min(answer, cost)                      # 이전 경우의 cost 합(answer)과 현재 경우에서 cost 합 비교
                                                        # 방문 표시는 초기화되어도 최소의 cost 합은 남아있는 형태
        return
    

    for i in range(x, n):                               # i 는 1 ~ n-1 범위
        for j in range(1, n):                           # j 는 1 ~ n-1 범위, (1,1), (1,2), ... 이런식으로 차례대로 돌 것임.
            
            if check(i, j):                             # 현위치, 상, 하, 좌,우 모두 방문된적 없고 범위를 벗어나지 않은 경우
                
                for dy, dx in flower_dir:               # 현위치, 상, 하, 좌, 우 위치를
                    visited[i+dy][j+dx] = True          # 방문 표시한다.

                dfs(i, cost + calculate(i,j), cnt + 1)  # 현재 위치에서의 cost 합과, 꽃이 핀 갯수를 누적해준다.

                for dy, dx in flower_dir:               # 현위치, 상, 하, 좌, 우 위치의
                    visited[i+dy][j+dx] = False         # 방문 표시 초기화하고 다음 지점을 기준으로 같은 액션을 반복한다.

# 시작
dfs(1, 0, 0)

print(answer)