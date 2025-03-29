n = int(input())

print(f'{chr((n + 8) % 12 + 65)}{((n + 6) % 10)}')