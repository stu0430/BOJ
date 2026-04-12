import sys

input = sys.stdin.readline

a, b = map(int, input().split())

result_b = b
power = 1
while (1 << power) <= b:
    result_b += (b // (1 << power)) * (1 << (power - 1))
    power += 1

a_minus = a - 1
result_a = a_minus
power = 1
while (1 << power) <= a_minus:
    result_a += (a_minus // (1 << power)) * (1 << (power - 1))
    power += 1

print(result_b - result_a)