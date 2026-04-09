import sys

input = sys.stdin.readline

n = int(input())
s = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

maze = [['#' for _ in range(101)] for _ in range(101)]
x, y, d = 50, 50, 0
min_x = max_x = x
min_y = max_y = y
maze[x][y] = '.'

for cmd in s:
    if cmd == 'L':
        d = (d + 3) % 4
        
    elif cmd == 'R':
        d = (d + 1) % 4
        
    elif cmd == 'F':
        x += dx[d]
        y += dy[d]
        maze[x][y] = '.'
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)

for i in range(min_x, max_x + 1):
    print(''.join(maze[i][min_y:max_y + 1]))