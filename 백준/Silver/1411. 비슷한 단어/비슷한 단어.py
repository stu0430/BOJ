import sys

input = sys.stdin.readline

n = int(input())
patterns = []

for _ in range(n):
    s = input().rstrip()
    char_map = {}
    pattern = []
    
    for char in s:
        if char not in char_map:
            char_map[char] = len(char_map)
        pattern.append(char_map[char])
    
    patterns.append(pattern)

result = 0
for i in range(n):
    for j in range(i + 1, n):
        if patterns[i] == patterns[j]:
            result += 1

print(result)