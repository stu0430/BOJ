import sys

input = sys.stdin.readline

word = input().rstrip()

result = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        result.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

result.sort()

print(result[0])