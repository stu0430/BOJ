l = int(input())
r = int(input())

result = 0
t = 1

while True:
    l = l * r // 100
    
    if l <= 5:
        break
    
    t *= 2
    result += l * t

print(result)