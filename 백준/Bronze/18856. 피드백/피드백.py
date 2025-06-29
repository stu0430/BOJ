n = int(input())

array = [0 for _ in range(n)]

array[0] = 1
array[1] = 2
array[-1] = 997

for i in range(1, n):
    if array[i] == 0 :
        array[i] = array[i - 1] + 1
    
print(n)
print(*array)