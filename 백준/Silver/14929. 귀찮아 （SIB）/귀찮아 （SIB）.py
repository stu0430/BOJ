n = int(input())
x = list(map(int, input().split()))

array = [x[0]]
for i in range(1, n):
    array.append(x[i] + array[i - 1])
    
result = 0
for i in range(n):
    result += x[i] * (array[n - 1] - array[i])

print(result)