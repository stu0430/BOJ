n = input()

array = [0] * 10

for i in n:
    array[int(i)] += 1

result = 0

for i in range(10):
    if i == 6 or i == 9:
        result = max(result, (array[6] + array[9] + 1) // 2)
        
    else:
        result = max(result, array[i])
        
print(result)