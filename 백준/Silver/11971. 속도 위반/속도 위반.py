a = []
b = []

n, m = map(int, input().split())

for _ in range(n):
    r, s = map(int, input().split())
    a.extend([s] * r)

for _ in range(m):
    r, s = map(int, input().split())
    b.extend([s] * r)

result = 0
for i in range(100):
    diff = b[i] - a[i]
    if diff > result:
        result = diff

print(result)