a, b = map(int, input().split())

result = 0
t = 0

for i in range (1, a + 1):
    result += i

t = result

for i in range(a + 1, b + 1):
    t += i
    result *= t

print(result % 14579)