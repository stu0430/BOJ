n, m = map(int, input().split())
for _ in range(n):
    input()

total = 0
for _ in range(m):
    t, p = map(int, input().split())
    total += p

print(f'{total / n:.5f}')