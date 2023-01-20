import sys

input = sys.stdin.readline

def dfs(x):
    global result
    
    if x > b:
        return
    
    if a <= x <= b:
        result += 1
        
    dfs(x * 10 + 4)
    dfs(x * 10 + 7)
    
a, b = map(int, input().split())

result = 0

dfs(4)
dfs(7)

print(result)