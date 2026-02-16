n, b = input().split()
b = int(b)

result = 0
for i, char in enumerate(n):
    digit = int(char) if char.isdigit() else ord(char) - ord('A') + 10
    result += digit * (b ** (len(n) - i - 1))

print(result)