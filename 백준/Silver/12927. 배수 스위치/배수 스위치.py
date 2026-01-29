l = list(input())
result = 0

for i in range(len(l)):
    if l[i] == 'Y':
        for j in range(i, len(l), i + 1):
            l[j] = 'N' if l[j] == 'Y' else 'Y'
        result += 1

print(result)