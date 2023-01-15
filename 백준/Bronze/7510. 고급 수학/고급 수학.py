import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    if a ** 2 + b ** 2 == c ** 2:
        print(f'Scenario #{i + 1}:')
        print('yes')
        print()
        
    elif a ** 2 + c ** 2 == b ** 2:
        print(f'Scenario #{i + 1}:')
        print('yes')
        print()
        
    elif b ** 2 + c ** 2 == a ** 2:
        print(f'Scenario #{i + 1}:')
        print('yes')
        print()
        
    else:
        print(f'Scenario #{i + 1}:')
        print('no')
        print()