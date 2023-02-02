import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(input().rstrip()) for i in range(n)]

result = 0

for i in range(n):
    for j in range(m):
        if array[i][j] == '-':
            if j == 0 or array[i][j - 1] == '|':
                result += 1
                
        elif array[i][j] == '|':
            if i == 0 or array[i - 1][j] == '-':
                result += 1
                
print(result)