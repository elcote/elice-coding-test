'''
1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

★★★
원래 에라토스테네스 체는 소수를 구하기 위함 인데,
이 문제는 삭제에만 초점을 맞춘 문제 소수이던 아니던 위와 같은 로직으로 차례차례 걸러낸다
★★★

'''

# 2, 3, 4(삭제), 5, 6(삭제), 7

# 2(삭제), 3(삭제), 4(삭제), 5(삭제), 6(삭제), 7(삭제), 8(삭제), 9(삭제), 10(삭제), 11, 12(삭제), 13, 14(삭제), 15(삭제)

import sys

input = sys.stdin.readline()

n, k = map(int, input.split())

cnt = 0

nums = [True] * (n + 1)         # [True, True, True, True, True, True, True, True] 0 부터 7 까지 인덱스
print(nums)

for i in range(2, len(nums)+1): # 2 부터 주어진 n까지 반복
    for j in range(i, n+1, i):  # from, to, by(증가폭)
        
        if nums[j] == True:     # 숫자가 살아있으면
            nums[j] = False     # 지우고
            cnt = cnt + 1       # cnt를 증가시켜준다.(몇번째로 지워졌는지 체크)
            if cnt == k:        # cnt 와 주어진 k가 같으면
                print(j)        # 출력해주고
                break           # 반복문 탈출