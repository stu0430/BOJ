s = input()
array = [[0, 0] for _ in range(26)]

for i in range(52):
    c = ord(s[i]) - ord('A')
    
    if array[c][0] == 0:
        array[c][0] = i + 1
        
    else:
        array[c][1] = i + 1

result = 0
for i in range(26):
    for j in range(26):
        if array[i][0] < array[j][0] < array[i][1] < array[j][1]:
            result += 1

print(result)