import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n + 1)]
result = []

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        result.append(v)
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = list(map(int, input().split()))

visited = [False for i in range(n + 1)]

S = [-1 for i in range(n + 1)]

for i in range(1, n + 1):
    S[order[i - 1]] = i

for i in range(1, n + 1):
    graph[i] = sorted(graph[i], key=lambda a: S[a])

bfs(graph, 1, visited)

if result == order:
    print(1)
else:
    print(0)