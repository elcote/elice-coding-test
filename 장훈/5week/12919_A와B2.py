from sys import stdin

def dfs(string):
    if len(string) == len(s):
        if string==s:
            print(1)
            exit(0)
        return

    if string[0]=='B':
        string = string[::-1]#문자열 뒤집기
        string.pop()#하나 빼기
        dfs(string)
        string.append('B')
        string=string[::-1]

    if string[-1]=='A':
        string.pop()
        dfs(string)
        string.append('A')

s, t = [list(stdin.readline().strip()) for _ in range(2)]
dfs(t)
print(0)