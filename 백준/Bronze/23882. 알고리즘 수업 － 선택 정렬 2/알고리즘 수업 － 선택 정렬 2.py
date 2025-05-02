n, k = map(int, input().split())
array = list(map(int, input().split()))

count = 0

for i in range(n - 1, 0, -1):
    max_idx = array.index(max(array[:i + 1]))
    
    if max_idx != i:
        array[max_idx], array[i] = array[i], array[max_idx]
        count += 1
        
        if count == k:
            print(*array)
            exit()
            
print(-1)