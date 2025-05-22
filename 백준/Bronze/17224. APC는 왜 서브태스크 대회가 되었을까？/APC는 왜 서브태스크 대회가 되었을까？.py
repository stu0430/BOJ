n, l, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

p = sorted(p, key=lambda x: x[1])

result = 0

for sub1, sub2 in p:
    if k == 0:
        break
    
    elif l >= sub2:
        result += 140
        k -= 1
        
    elif l >= sub1:
        result += 100
        k -= 1

print(result)