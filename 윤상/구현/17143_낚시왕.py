from copy import deepcopy
import sys

def input():
    return sys.stdin.readline().rstrip()

# R = 격자판의 행의 수
# C = 격자판의 열의 수
# M = 상어의 총 마리수
R, C, M = map(int, input().split())

class Shark():
    def __init__(self, row, col, speed, direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.speed = speed
    # 상어의 움직임 방향과 속도를 기준으로 일단 움직여줌
    def moveSharks(self):
        if self.direction == 1:
            self.row = self.row - self.speed
        elif self.direction == 2:
            self.row = self.row + self.speed
        elif self.direction == 3:
            self.col = self.col + self.speed
        elif self.direction == 4:
            self.col = self.col - self.speed
    def adjustSharkLocationPointer(self):
        while self.row > R or self.row < 1:
            if self.direction == 1 and self.row < 1:
                self.row = -self.row + 2
                self.direction = 2
            if self.direction == 2 and self.row > R:
                self.row = R - abs(self.row - R)
                self.direction = 1
        while self.col > C or self.col < 1:
            if self.direction == 3 and self.col > C:
                self.col = C - abs(self.col - C)
                self.direction = 4
            if self.direction == 4 and self.col < 1:
                self.col = -self.col + 2
                self.direction = 3

Sharks = {}
board = [[0] * (C+1) for _ in range(R+1)]
for _ in range(M):
    row, col, speed, direction, size = map(int, input().split())
    Sharks[size] = Shark(row, col, speed, direction)
    board[row][col] = size

score = 0

for j in range(1,C+1):
    for i in range(1,R+1):
        if board[i][j]:
            score += board[i][j]
            del Sharks[board[i][j]]
            board[i][j] = 0
            break
    elimination_list = [[0]* (C+1) for _ in range(R+1)]
    remove_list = []
    for size, shark in Sharks.items():
        shark.moveSharks()
        shark.adjustSharkLocationPointer()
        if elimination_list[shark.row][shark.col]:
            if elimination_list[shark.row][shark.col] > size:
                remove_list.append(size)
            else:
                remove_list.append(elimination_list[shark.row][shark.col])
                elimination_list[shark.row][shark.col] = size
        else:
            elimination_list[shark.row][shark.col] = size
    for target in remove_list:
        del Sharks[target]
    board = deepcopy(elimination_list)
        
print(score)