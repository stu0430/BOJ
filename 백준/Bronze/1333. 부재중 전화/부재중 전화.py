n, l, d = map(int, input().split())

t = []

for i in range(n):
    t.extend([True] * l)
    
    if i < n - 1:
        t.extend([False] * 5)

result = 0

while result < len(t) and t[result]:
    result += d

print(result)