import sys

input = sys.stdin.readline

array = [list(input().split()) for i in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = set()

def dfs(x, y, s):
    if len(s) == 6:
        result.add(s)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, s + array[nx][ny])
            
for i in range(5):
    for j in range(5):
        dfs(i, j, array[i][j])
        
print(len(result))