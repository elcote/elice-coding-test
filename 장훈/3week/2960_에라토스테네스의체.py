#에라토스테네스의 체

N, K = map(int, input().split())

check=[False for _ in range(N+2)]

cnt=0

for i in range(2, N+1):
    if check[i]==False:#false는 값이있다면이라는 의미?
        for j in range(i, N+1, i):
            if check[j]==False:#값이 있다면 True로 True는그값을 지운다는의미
                check[j]=True
                cnt+=1#지우는 횟수

                if cnt==K:
                    print(j)
                    break
