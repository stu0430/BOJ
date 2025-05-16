import sys

input = sys.stdin.readline

n = int(input())
result = 0

for i in range(n, 0, -1):
    result += n / i

print(f'{result:.20f}')