'''
    문제 이름 : 도영이가 만든 맛있는 음식
    문제 번호 : 2961
    문제 링크 : https://www.acmicpc.net/problem/2961
'''
import sys
from itertools import combinations
read = sys.stdin.readline

'''
음식의 신맛 = 재료의 신맛의 곱
음식의 쓴맛 = 재료의 쓴맛의 합
신맛과 쓴맛의 차이가 가장 작은 요리

시간 제한 : 1초
메모리 제한 : 
결과값 최대 <= 1,000,000,000 

신맛과 쓴맛 차이가 기존 최소값보다 작을경우 교체
'''

n = int(read())
min_result = 1000000001 #초기 최소값 세팅

arr=[]

for _ in range(n):
    arr.append(list(map(int, read().split(" "))))

all_com = []    #모든 조합을 담을 배열
for i in range(1, n+1):
    all_com.append(combinations(arr, i))

for line in all_com:
    for each in line:
        sour_t = 1;
        bitter_t = 0;
        for e in each:
            sour_t *= e[0]
            bitter_t += e[1]
        min_result = min(abs(sour_t-bitter_t),min_result)
print(min_result)

'''
틀렸던 풀이

sour = []       #신맛을 담을 배열
bitter = []     #쓴맛을 담을 배열

for i in range(n):
    x,y = map(int,read().split())
    sour.append(x)
    bitter.append(y)

for i in range(len(sour)):  #입력된 데이터 길이만큼
    sour_level = sour[i]    
    bitter_level = bitter[i]
    for j in range(i+1,len(sour)):
        if i==j:
            continue
        sour_level *= sour[j]
        bitter_level += bitter[j]
    min_result = min(min_result,abs(sour_level-bitter_level))

print(min_result)
'''