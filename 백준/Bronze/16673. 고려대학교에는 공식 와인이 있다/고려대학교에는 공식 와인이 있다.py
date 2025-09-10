c, k, p = map(int, input().split())
result = 0

for n in range(c + 1):
    result += k * n + p * n * n

print(result)