import sys

input = sys.stdin.readline

array = [list(input().rstrip()) for i in range(8)]

result = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and array[i][j] == 'F':
            result += 1

print(result)