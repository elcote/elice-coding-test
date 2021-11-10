import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

stairs=[] # 층별 점수를 담는 배열
DP = [0 for _ in range(N)] # 각 층별 까지의 최대값을 담는 배열
# stepped = [False for _ in range(N)] # 해당 층을 밟았는지, 밟지 않았는지 체크
# stepped[-1] = True # 마지막 도착 계단은 무조건 밟음

for i in range(N):
    weight = int(input())
    stairs.append(weight)
    if i == 0:
        DP[0] = weight # 첫번째 계단에서는 이 값이 무조건 최대값임

if N >= 2:
    DP[1] = DP[0] + stairs[1]
if N >= 3:
    DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
# 계단은 한번에 한계단씩 또는 두 계단씩 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. (시작점 계단은 포함안됨)

for i in range(3,N):
    DP[i] = max(DP[i-2] + stairs[i], DP[i-3] + stairs[i-1] + stairs[i])
# print(stairs)
# print(DP)
print(DP[-1])