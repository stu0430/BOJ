n, m = map(int, input().split())
array = list(map(int, input().split()))
result = 1

for i in array:
    result *= i % m
    
print(result % m)
