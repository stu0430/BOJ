n, k = map(int, input().split())
array = [[0] * 6 for _ in range(2)]
result = 0

for _ in range(n):
    s, y = map(int, input().split())
    array[s][y - 1] += 1

for i in range(2):
    for j in range(6):
        result += (array[i][j] + k - 1) // k

print(result)