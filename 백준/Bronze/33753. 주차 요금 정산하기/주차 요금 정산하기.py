from math import ceil

a, b, c = map(int, input().split())
t = int(input())

result = a if t > 0 else 0
t = max(0, t - 30)

result += ceil(t / b) * c

print(result)