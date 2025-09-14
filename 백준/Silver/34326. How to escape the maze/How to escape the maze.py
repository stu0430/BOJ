import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [input().rstrip() for _ in range(n)]

start_pos = None
end_pos = None

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'S':
            start_pos = (i, j)
            
        elif maze[i][j] == 'E':
            end_pos = (i, j)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_initial_direction(pos):
    r, c = pos
    
    for i, (dr, dc) in enumerate(directions):
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != '*':
            return i
        
    return 0

def can_move(pos, direction):
    r, c = pos
    dr, dc = directions[direction]
    nr, nc = r + dr, c + dc
    return 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != '*'

def move(pos, direction):
    r, c = pos
    dr, dc = directions[direction]
    return (r + dr, c + dc)

pos = start_pos
direction = find_initial_direction(pos)
left_steps = 0

while pos != end_pos:
    direction = (direction - 1) % 4
    
    while not can_move(pos, direction):
        direction = (direction + 1) % 4
    
    pos = move(pos, direction)
    left_steps += 1
    
    if left_steps > n * m * 4:
        left_steps = float('inf')
        break

pos = start_pos
direction = find_initial_direction(pos)
right_steps = 0

while pos != end_pos:
    direction = (direction + 1) % 4
    
    while not can_move(pos, direction):
        direction = (direction - 1) % 4

    pos = move(pos, direction)
    right_steps += 1
    
    if right_steps > n * m * 4:
        right_steps = float('inf')
        break

if left_steps < right_steps:
    print('LEFT IS BEST')
    
elif right_steps < left_steps:
    print('RIGHT IS BEST')
    
else:
    print('SAME')