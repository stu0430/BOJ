n, m = map(int, input().split())
b = [input() for _ in range(n)]

for i in range(n):
    print(b[i][::-1])