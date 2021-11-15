'''

<소수 & 팰린드롬>

어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.

어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

-입력-
31


-출력-
101

# 1. 에라토스테네스의 체 구현
# 2. 문자열로 바꿔서 팰린드롬 수 인지 확인하고
# 3. 1,2 에 모두 해당되면 출력한다.

'''

# 런타임 에러 (IndexError)

import sys

def input():
    return sys.stdin.readline()

n = int(input())        
m = int(1000001)

temp_list = m * [True]
temp_list[0] = False                         # 0과
temp_list[1] = False                         # 1은 소수가 아니므로 False로 미리 바꿔줍니다.



for i in range(2, int(m**0.5)+1):            # 에라토스테네스의 체로 걸러줍니다.
    for j in range(i+i, len(temp_list), i):
        if(temp_list[j] == True):            # 소수이면 True로 남고
            temp_list[j] = False             # 소수가 아니면 False로 바뀝니다.
        
i = int(n)
while(True):
    if(int(i) > n and temp_list[i] == True): # i 가 n 보다 크고 소수인 수를
        temp = str(i)                        # 문자열 i로 바꿔주고
        if(temp == temp[::-1]):              # 팰린드롬 수인지 판단하여 맞으면
            result = temp
            print(result)                      # 그 수를 출력해줍니다.
            break
    i += 1
