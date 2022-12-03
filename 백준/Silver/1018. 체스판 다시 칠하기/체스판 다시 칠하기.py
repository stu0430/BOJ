import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(input().rstrip()) for i in range(n)]

result = []

for i in range(n - 7):
    for j in range(m - 7):
        count = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if array[k][l] == 'B':
                        count += 1
                else:
                    if array[k][l] == 'W':
                        count += 1
        result.append(count)
        result.append(64 - count)
        
print(min(result))