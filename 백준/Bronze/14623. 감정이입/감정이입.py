b1 = list(input())
b2 = list(input())

result = [0] * (len(b1) + len(b2))

for i in range(len(b2)):
    for j in range(len(b1)):
        result[i + j + 1] += int(b1[j]) * int(b2[i])

t = 0

for i in range(len(result) - 1, -1, -1):
    result[i] += t
    
    if result[i] > 1:
        b1 = result[i]
        result[i] = result[i] % 2
        t = b1 // 2
    else:
        t = 0

while result[0] == 0:
    result.pop(0)

print(''.join(map(str, result)))