n=int(input())

for _ in range(n):
    check=input()
    ls = list(check)
    sum=0
    for i in ls:
        if i=="(":
            sum+=1
        elif i==")":
            sum-=1
        if sum<0:
            print("NO")
            break

    if sum>0:
        print("NO")
    elif sum==0:
        print("YES")