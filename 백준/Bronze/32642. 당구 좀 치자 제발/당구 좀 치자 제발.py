n = int(input())
array = list(map(int, input().split()))

a, result = 0, 0

for i in array:
    if i < 1:
        a -= 1
        
    else:
        a += 1
        
    result += a
    
print(result)