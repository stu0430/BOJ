n, k = map(int, input().split())
array = list(map(int, input().split(',')))

for _ in range(k):
    array = [array[i + 1] - array[i] for i in range(len(array) - 1)]
    
print(*array, sep=',')