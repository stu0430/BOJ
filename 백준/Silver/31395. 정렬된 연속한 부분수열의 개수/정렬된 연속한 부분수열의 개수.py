n = int(input())
array = list(map(int, input().split()))

results = [1] * n

for i in range(1, n):
    if array[i] > array[i - 1]:
        results[i] = results[i - 1] + 1

result = sum(results)

print(result)