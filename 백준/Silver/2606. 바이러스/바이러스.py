import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n+1):
    graph[i].sort()
    
visited = [False] * (n+1)

def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
 
print(len(result)-1)