n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort()

cost = 10001
result = 0

for c in array:
    temp = c[1]
    
    if temp < cost:
        cost = temp
        result += 1
        
print(result)