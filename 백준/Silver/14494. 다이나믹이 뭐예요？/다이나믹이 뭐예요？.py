import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [[0] * (m + 1) for _ in range(n + 1)]

array[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            continue
            
        array[i][j] = array[i - 1][j] + array[i][j - 1] + array[i - 1][j - 1]
        
print(array[n][m] % 1000000007)