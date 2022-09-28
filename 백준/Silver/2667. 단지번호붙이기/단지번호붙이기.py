import sys

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().rstrip())))
    
result = [0] * 25

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        result[-1] += 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(0)
            count += 1
        
print(count)

result.sort()

for i in result:
    if i != 0:
        print(i)