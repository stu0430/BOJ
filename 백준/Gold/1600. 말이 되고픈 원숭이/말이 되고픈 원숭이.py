import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

horse_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
normal_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 0

    while queue:
        y, x, horse_used = queue.popleft()
        
        if y == h - 1 and x == w - 1:
            return visited[y][x][horse_used]

        if horse_used < k:
            for dy, dx in horse_moves:
                ny, nx = y + dy, x + dx
                if 0 <= ny < h and 0 <= nx < w and not graph[ny][nx] and visited[ny][nx][horse_used + 1] == -1:
                    visited[ny][nx][horse_used + 1] = visited[y][x][horse_used] + 1
                    queue.append((ny, nx, horse_used + 1))
        
        for dy, dx in normal_moves:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not graph[ny][nx] and visited[ny][nx][horse_used] == -1:
                visited[ny][nx][horse_used] = visited[y][x][horse_used] + 1
                queue.append((ny, nx, horse_used))

    return -1

print(bfs())