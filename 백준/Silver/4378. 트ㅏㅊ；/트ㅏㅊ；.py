import sys

keyboard = [
    "`1234567890-=",
    "QWERTYUIOP[]\\",
    "ASDFGHJKL;'",
    "ZXCVBNM,./"
]

for line in sys.stdin:
    result = []
    for char in line.rstrip('\n'):
        if char == ' ':
            result.append(' ')
        else:
            found = False
            for row in keyboard:
                if char in row:
                    idx = row.index(char)
                    if idx > 0:
                        result.append(row[idx - 1])
                    found = True
                    break
            if not found:
                result.append(char)
    print(''.join(result))