a, b = map(int, input().split())

if a - b > 0:
    print(2 * (a - b) // b)
else:
    print(-2 * (a - b) // b)