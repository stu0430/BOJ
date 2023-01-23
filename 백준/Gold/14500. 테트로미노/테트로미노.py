import sys

input = sys.stdin.readline

def dfs(x, y, count, sum):
    global result
    
    if count == 4:
        result = max(result, sum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
            continue
        
        visited[nx][ny] = True
        
        dfs(nx, ny, count + 1, sum + array[nx][ny])
        
        visited[nx][ny] = False
            
n, m = map(int, input().split())

array = [list(map(int, input().split())) for i in range(n)]

result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited= [[False] * m for i in range(n)]
            
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        
        dfs(i, j, 1, array[i][j])
        
        visited[i][j] = False
        
        if j <= m - 3 and i <= n - 2:
            result = max(result, sum(array[i][j:j + 3]) + array[i + 1][j + 1])
            
        if 1 <= j <= m - 2 and i <= n - 2:
            result = max(result, sum(array[i + 1][j - 1:j + 2]) + array[i][j])
            
        if j <= m - 2 and i <= n - 3:
            result = max(result, array[i][j] + array[i + 1][j] + array[i + 2][j] + array[i + 1][j + 1])
            
        if 1 <= i < n - 2 and j <= m - 2:
            result = max(result, array[i][j] + array[i - 1][j + 1] + array[i][j + 1] + array[i + 1][j + 1])
        
print(result)