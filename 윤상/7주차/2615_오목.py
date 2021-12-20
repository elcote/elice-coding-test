import sys

def input():
    return sys.stdin.readline().rstrip()

maps = []
visited = [[False] * 19 for _ in range(19)]
white = []
black = []
di = [(0,0),(1,0),(0,1),(1,1), (-1,1)]
black_flag = False
white_flag = False
ans_i = 0
ans_j = 0

def dfs(i,j, color, cnt, direction):
    global black_flag, white_flag
    if direction == 0:
        for d in di[1:]:
            ni = i + d[0]
            nj = j + d[1]
            direction += 1
            if 0 <= ni <= 18 and 0 <= nj <= 18:
                if color == 1:
                    if (ni,nj) in black:
                        dfs(ni,nj,1,cnt+1,direction)
                elif color == 2:
                    if (ni,nj) in white:
                        dfs(ni,nj,2,cnt+1,direction)
    else:
        ni = i + di[direction][0]
        nj = j + di[direction][1]
        if 0 <= ni <= 18 and 0 <= nj <= 18 and maps[ni][nj] == color:
                if color == 1:
                    if (ni,nj) in black:
                        dfs(ni,nj,1,cnt+1,direction)
                elif color == 2:
                    if (ni,nj) in white:
                        dfs(ni,nj,2,cnt+1,direction)
        else:
            if cnt == 5:
                if direction == 1:
                    row_up = i - 5
                    col_up = j
                elif direction == 2:
                    row_up = i
                    col_up = j - 5
                elif direction == 3:
                    row_up = i - 5
                    col_up = j - 5
                elif direction == 4:
                    row_up = i + 5
                    col_up = j - 5
                
                if color == 1 and (row_up, col_up) not in black:
                    # print("BLACKFLAG!!!!")
                    # print(i, j)
                    black_flag = True
                if color == 2 and (row_up, col_up) not in white:
                    # print("WHITEFLAG!!!!")
                    white_flag = True
for i in range(19):
    line = list(map(int, input().split()))
    maps.append(line)
    for j in range(len(line)):
        if line[j] == 1:
            black.append((i,j))
        elif line[j] == 2:
            white.append((i,j))
            
for black_stone in black:
    i = black_stone[0]
    j = black_stone[1]
    dfs(i, j, 1, 1,0)
    if black_flag:
        ans_i = i+1
        ans_j = j+1
        break

for white_stone in white:
    i = white_stone[0]
    j = white_stone[1]
    dfs(i, j, 2, 1,0)
    if white_flag:
        ans_i = i+1
        ans_j = j+1
        break

if black_flag:
    print(1)
    print(ans_i, ans_j)
elif white_flag:
    print(2)
    print(ans_i, ans_j)
else:
    print(0)