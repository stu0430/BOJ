n, m, l = map(int, input().split())

result = 0
index = 0
array = [0] * n 

while array[index] < m - 1:
    array[index] += 1
    result += 1
    index = (index + l) % n if array[index] % 2 == 1 else (index - l) % n

print(result)