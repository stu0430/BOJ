n = int(input())

total = sum(list(map(int, input().split())))
total += (n - 1) * 8

print(total // 24, total % 24)