n = int(input())
h = list(map(int, input().split()))

result = 1

for i in range(n - 1):
    if h[i] <= h[i + 1]:
        result += 1

print(result)