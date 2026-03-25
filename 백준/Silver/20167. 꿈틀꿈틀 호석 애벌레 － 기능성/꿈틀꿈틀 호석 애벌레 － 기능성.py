import sys

input = sys.stdin.readline

def dfs(d, s, p, n, k, array):
    global result
    
    if d == n:
        result = max(result, s)
        return
    
    np = p + array[d]
    
    if np >= k:
        dfs(d + 1, s + (np - k), 0, n, k, array)
    else:
        dfs(d + 1, s, np, n, k, array)
        
    dfs(d + 1, s, 0, n, k, array)

n, k = map(int, input().split())
array = list(map(int, input().split()))
result = 0

dfs(0, 0, 0, n, k, array)

print(result)