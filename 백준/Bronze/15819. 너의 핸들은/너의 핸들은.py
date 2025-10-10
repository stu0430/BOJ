n, i = map(int, input().split())
print(sorted([input() for _ in range(n)])[i - 1])