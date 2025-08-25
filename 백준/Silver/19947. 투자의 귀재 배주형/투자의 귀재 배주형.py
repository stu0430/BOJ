h, y = map(int, input().split())

d = [0] * 16
d[5] = h

for i in range(6, 16):
    d[i] = max(max(int(d[i - 1] * 1.05), int(d[i - 3] * 1.2)), int(d[i - 5] * 1.35))
    
print(int(d[y + 5]))