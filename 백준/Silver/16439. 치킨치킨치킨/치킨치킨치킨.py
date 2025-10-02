import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

result = 0

for cols in combinations(range(m), 3):
    total = sum(max(array[i][cols[0]], array[i][cols[1]], array[i][cols[2]]) for i in range(n))
    result = max(result, total)

print(result)