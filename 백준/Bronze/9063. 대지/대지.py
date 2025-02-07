n = int(input())
x, y = zip(*(map(int, input().split()) for _ in range(n)))

dx = max(x) - min(x)
dy = max(y) - min(y)

print(dx * dy)