n = int(input())
result = 1

s = set()
s.add('ChongChong')

for _ in range(n):
    a, b = input().split()
    
    if (a in s) ^ (b in s):
        result += 1
        
        s.add(a)
        s.add(b)

print(result)