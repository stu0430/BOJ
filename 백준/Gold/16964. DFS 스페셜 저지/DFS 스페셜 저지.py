import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n + 1)]
result = []

def dfs(graph, v, visited) :
    if visited[v] == True:
        return
    visited[v] = True
    result.append(v)
    for i in graph[v] :
        if visited[i] == False :
            dfs(graph, i, visited)

for i in range(n - 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
order = list(map(int,input().split()))

visited = [False for i in range(n + 1)]

S = [-1 for i in range(n + 1)]

for i in range(1, n + 1):
    S[order[i - 1]] = i
    
for i in range(1, n + 1):
    graph[i] = sorted(graph[i], key=lambda a: S[a])
    
dfs(graph, 1, visited)

if result == order:
    print(1)
else:
    print(0)