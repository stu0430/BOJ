import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = list(map(int, input().split()))

result = -1

def dfs(x):
    global result
    
    if x > n:
        return
    
    result = max(result, x)
    
    for i in array:
        dfs(10 * x + i)
        
dfs(0)
print(result)