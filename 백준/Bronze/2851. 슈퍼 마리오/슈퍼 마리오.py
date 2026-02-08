result = 0
prev = 0

for _ in range(10):
    score = int(input())
    prev = result
    result += score
    
    if result >= 100:
        if abs(100 - prev) < abs(100 - result):
            result = prev
        break

print(result)