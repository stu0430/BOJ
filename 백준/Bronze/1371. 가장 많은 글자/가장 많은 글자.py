import sys

alpha = [0] * 26

for line in sys.stdin:
    words = line.split()
    for word in words:
        for char in word:
            alpha[ord(char) - 97] += 1

max_count = max(alpha)

result = []
for i in range(26):
    if alpha[i] == max_count:
        result.append(chr(i + 97))

print(''.join(result))