n, m = map(int, input().split())

array = [0] * n

for i in range(m):
    i, j, k = map(int, input().split())
    
    for l in range(i - 1, j):
        array[l] = k
        
print(*array)