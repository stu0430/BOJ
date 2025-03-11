array = list(map(int, input().split()))
array.sort()

if array[0] + array[1] > array[2]:
    print(sum(array))
    
else:
    print((array[0] + array[1]) * 2 - 1)