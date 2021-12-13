# n = int(input())
# tmp = []

# for i in range(n):
#     s, b = map(int,input().split(' '))
#     tmp.append((s,b))

# tmp.sort(key = lambda x :abs(x[1] - x[0]))
# print(tmp)

# x, y = tmp[0][0], tmp[0][1]
# for i in range(1,n):
#     ss = tmp[i][0]
#     bb = tmp[i][1]
#     if abs(ss * x - (bb + y)) < abs(x - y):
#         x *= ss
#         y += bb
#     print(x,y)

# print(x,y)
# print(abs(x - y))




# from math import dist
# import math

# def solution(x,y):
#     ans = 0
#     xy = []
#     for i in range(len(x)):
#         xy.append([x[i],y[i]])
#     xy = sorted(xy,key=lambda a: (a[0],a[1]))

#     for i in range(len(xy) - 1):
#         tmp = dist(xy[i],xy[i+1])
#         print(tmp)
#         if tmp > ans:
#             ans = tmp
    
#     return math.ceil(ans)




# print(solution([0,10,10,0],[0,0,10,20]))
# print(solution([1,2,4,2],[0,0,4,2]))