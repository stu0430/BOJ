import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

array = [i for i in range(1, n + 1)]

result = []

x = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  
    
for i in range(n + 1):
    graph[i].sort()
    
visited = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)
    array.remove(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
               
if len(array) != 0:
    while len(array) != 0:
        dfs(graph, array[0], visited)
        x.append(result)
        result = []

print(len(x))