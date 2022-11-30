import sys

input = sys.stdin.readline

r, c, w = map(int, input().split())

array = [[0] * i for i in range(1, 31)]

for i in range(30):
    for j in range(i + 1):
        if j == 0 or j == i:
            array[i][j] = 1
        else:
            array[i][j] = array[i - 1][j - 1] + array[i - 1][j]

result = 0

for i in range(w):
    for j in range(i + 1):
        result += array[r + i - 1][c + j - 1]

print(result)