n, h = map(int, input().split())
d = list(map(int, input().split()))
t = 0

for i in range(n):
    t += d[i]
    if t >= h:
        print(i + 1)
        exit()
        
if t < h:
    print(-1)