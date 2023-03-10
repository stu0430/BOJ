array = [0] * 4

for i in range(4):
    a, b = map(int, input().split())
    
    array[i] = array[i - 1] - a + b

print(max(array))