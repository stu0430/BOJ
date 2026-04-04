import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

house = [(x, y) for x in range(n) for y in range(n) if board[x][y] == 1]
chicken = [(x, y) for x in range(n) for y in range(n) if board[x][y] == 2]

def city_chicken_distance(selected):
    total = 0
    
    for hx, hy in house:
        total += min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected)
        
    return total

result = min(city_chicken_distance(chks) for chks in combinations(chicken, m))
print(result)