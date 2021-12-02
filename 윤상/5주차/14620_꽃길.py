import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

garden = []

for i in range(N):
    line = list(map(int,input().split()))
    garden.append(line)
pos = []
for i in range(1,N-1):
    for j in range(1,N-1):
        pos.append((i,j))

possible = combinations(pos, 3)
di = [(-1,0),(1,0),(0,-1),(0,1),(0,0)]
summ = 3000
for d in possible:
    first = d[0]
    second = d[1]
    third = d[2]
    
    f_s_dis = abs(first[0]-second[0]) + abs(first[1]-second[1])
    f_t_dis = abs(first[0]-third[0]) + abs(first[1]-third[1])
    s_t_dis = abs(second[0]-third[0]) + abs(second[1]-third[1])
    
    if f_s_dis >= 3 and f_t_dis >= 3 and s_t_dis >= 3:
        tmp = 0
        for d in di:
            tmp += garden[first[0] + d[0]][first[1] + d[1]]
            tmp += garden[second[0] + d[0]][second[1] + d[1]]
            tmp += garden[third[0] + d[0]][third[1] + d[1]]
        if summ > tmp:
            summ = tmp
print(summ)