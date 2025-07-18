n = int(input())
k = int(input())

array = [0 for _ in range(n + 1)]

for i in range(2, n + 1):
    if array[i] == 0:
        for j in range(i, n + 1, i):
            if j % i == 0:
                array[j] = max(array[j], i)
result = 0
for i in array:
    if i <= k:
        result += 1
        
print(result - 1)