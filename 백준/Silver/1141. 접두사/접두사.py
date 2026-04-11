n = int(input())
words = set(input().strip() for _ in range(n))
words = list(words)

result = 0
for w in words:
    if not any(w != other and other.startswith(w) for other in words):
        result += 1

print(result)