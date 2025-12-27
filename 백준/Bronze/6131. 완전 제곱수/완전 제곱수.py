n = int(input())
result = 0

for i in range(1, 1001):
    for j in range(1, 1001):
        if (i * i) - (j * j) == n:
            result += 1
            
print(result)