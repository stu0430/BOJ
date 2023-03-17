n = int(input())

result = 0

for i in range(1, n + 1):
    result += 1.5 * i * (i + 1)
    
print(int(result))