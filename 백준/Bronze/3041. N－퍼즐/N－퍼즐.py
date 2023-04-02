def abs(a, b):
    return a - b if a > b else b - a

array = [input() for _ in range(4)]

result = 0
for i in range(4):
    for j in range(4):
        if array[i][j] != '.':
            result += abs(i, (ord(array[i][j]) - ord('A')) // 4) + abs(j, (ord(array[i][j]) - ord('A')) % 4)
            
print(result)