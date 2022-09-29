import sys

input = sys.stdin.readline

s = input().rstrip()

result = []

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        result.append(s[i:j])
        
print(len(set(result)))