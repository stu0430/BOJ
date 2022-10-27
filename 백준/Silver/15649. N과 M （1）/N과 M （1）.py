import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [i for i in range(1, n + 1)]

result = []

def dfs(array, result):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(len(array)):
        dfs(array[:i] + array[i + 1:], result + [array[i]])
        
dfs(array, result)