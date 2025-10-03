n = int(input())

s = set()
a = 0

for i in range(1, n + 1):
    s.add(a)
    t = a - i
    
    if t < 0 or t in s:
        t = a + i
    
    a = t

print(a)