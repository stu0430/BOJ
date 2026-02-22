c, r = map(int, input().split())
k = int(input())

if k > c * r:
    print(0)
    exit()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visit = [[False] * c for _ in range(r)]
x, y = 0, 0
d = 0

for i in range(1, c * r + 1):
    if i == k:
        print(x + 1, y + 1)
        break
    
    visit[y][x] = True
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    if nx < 0 or ny < 0 or nx >= c or ny >= r or visit[ny][nx]:
        d = (d + 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]
        
    x, y = nx, ny