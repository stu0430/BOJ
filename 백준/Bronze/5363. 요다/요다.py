n = int(input())

for _ in range(n):
    s = list(input().split())
    print(*s[2:] + s[:2])