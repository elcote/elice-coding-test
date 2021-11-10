from copy import deepcopy


class Shark:
    def __init__(self, row, col, spd, dir):
        self.row = row
        self.col = col
        self.spd = spd % (2 * (R - 1, C - 1)[(dir - 1) // 2])
        self.dir = dir

    def move(self, v):
        data = {1: [(-1, 0), 0, 2], 2: [(1, 0), R - 1, 1],
                3: [(0, 1), C - 1, 4], 4: [(0, -1), 0, 3]}
        rc, bound, next_dir = data[self.dir]
        rest = bound - (self.row * rc[0] + self.col * rc[1])
        if v < rest:
            self.row += rc[0] * v
            self.col += rc[1] * v
        else:
            self.row = bound if rc[0] else self.row
            self.col = bound if rc[1] else self.col
            self.dir = next_dir
            self.move(v - rest)


R, C, M = map(int, input().split())
sharks = {}
board = [[0] * C for _ in range(R)]
a = Shark(3, 0, 3, 3)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[z] = Shark(r - 1, c - 1, s, d)
    board[r - 1][c - 1] = z

total_size = 0
for j in range(C):
    # catch sharks
    for i in range(R):
        if board[i][j]:
            total_size += board[i][j]
            del sharks[board[i][j]]
            board[i][j] = 0
            break

    # move each sharks
    new_board = [[0] * C for _ in range(R)]
    terminate = []
    for size, shark in sharks.items():
        shark.move(shark.spd)
        if new_board[shark.row][shark.col]:
            if new_board[shark.row][shark.col] > size:
                terminate.append(size)
            else:
                terminate.append(new_board[shark.row][shark.col])
                new_board[shark.row][shark.col] = size
        else:
            new_board[shark.row][shark.col] = size

    for t in terminate:
        del sharks[t]
    board = deepcopy(new_board)
print(total_size)