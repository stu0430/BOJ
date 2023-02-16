import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    
    print(f'Scenario #{i + 1}:')
    print(b * (b + 1) // 2 - abs(a) * (abs(a) + 1) // 2 if a < 0 else b * (b + 1) // 2 - (a - 1) * a // 2)
    print()