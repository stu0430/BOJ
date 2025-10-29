n = int(input())

total = 0
total_cubed = 0

for i in range(1, n + 1):
    total += i
    total_cubed += i ** 3

print(total)
print(total ** 2)
print(total_cubed)