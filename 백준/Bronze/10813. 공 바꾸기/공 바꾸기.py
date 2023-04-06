n, m = map(int, input().split())

array = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    array[i - 1], array[j - 1] = array[j - 1], array[i - 1]
    
print(*array)