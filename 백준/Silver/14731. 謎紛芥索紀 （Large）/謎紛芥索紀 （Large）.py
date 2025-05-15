n = int(input())
result = 0

for _ in range(n):
    a, b = map(int, input().split())
    c = (a * b % 1000000007) * pow(2, b - 1, 1000000007) % 1000000007
    result = (result + c) % 1000000007

print(result)