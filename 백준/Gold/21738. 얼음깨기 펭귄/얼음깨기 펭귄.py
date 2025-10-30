import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node, level):
    visited[node] = True
    
    if node == p:
        visited[p] = False
        
        if len(length) < 2:
            length.append(level)
            
        elif level < max(length):
            length.remove(max(length))
            length.append(level)
            
        return
    
    for next_node in tree[node]:
        if not visited[next_node]:
            dfs(next_node, level + 1)

n, s, p = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n + 1)
length = []

for i in range(1, s + 1):
    if not visited[i] and i != p:
        dfs(i, 0)

print(n - sum(length) - 1)