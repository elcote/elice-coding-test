import sys
input=sys.stdin.readline

trees={}#나무의 이름을 key, 나무의 수를 value
n=0

while True:
    tree=input().rstrip()
    if not tree:#나무가 입려되지 않았다면 break
        break
    if tree in trees:#나무의 이름이 있다면 value1증가
        trees[tree] +=1
    else:#나무의 이름이 없다면 value를 1로 지정
        trees[tree]=1
    n+=1#n은 나무가 입력된 총 횟수
tree_list = list(trees.keys())#나무이름들을 list로 지정후 사전순 정렬
tree_list.sort()

for tree in tree_list:#나무의 비율 출력 %.4f로 4째자리까지 반올림 
    print('%s %.4f' %(tree, trees[tree]/n*100))