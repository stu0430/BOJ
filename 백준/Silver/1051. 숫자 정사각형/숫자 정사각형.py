import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(input().rstrip()) for i in range(n)]

result = 1

for i in range(n):
    for j in range(m):
        for k in range(1, min(n, m)):
            if i + k < n and j + k < m:
                if array[i][j] == array[i][j + k] == array[i + k][j] == array[i + k][j + k]:
                    result = max(result, k + 1)
                    
print(result ** 2)