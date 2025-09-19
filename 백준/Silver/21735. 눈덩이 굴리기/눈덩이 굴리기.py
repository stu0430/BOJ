import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

result = -1

def dfs(i, s, t):
    global result
    
    if t > m:
        return
    
    if t <= m:
        result = max(result, s)
    
    if i <= n - 1:
        dfs(i + 1, s + a[i + 1], t + 1)
    
    if i <= n - 2:
        dfs(i + 2, (s // 2) + a[i + 2], t + 1)

dfs(0, 1, 0)
print(result)