p = {i + 1:(2024 + (8 + 7 * i - 1) // 12, (8 + 7 * i - 1) % 12 + 1) for i in range(5)}
print(*p[int(input())])