k, l = map(int, input().split())
k = k % 26
s = input()

result = []

for i in s:
    if 'A' <= i <= 'Z':
        result.append(chr(ord('A') + ((ord(i) - ord('A') + k + 26) % 26)))
    elif 'a' <= i <= 'z':
        result.append(chr(ord('a') + ((ord(i) - ord('a') + k + 26) % 26)))
    else:
        result.append(i)

print(''.join(result))