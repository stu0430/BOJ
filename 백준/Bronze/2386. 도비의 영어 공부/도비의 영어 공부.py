import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '#':
        break
    
    c, s = s[0], s[2:]
    
    result = 0
    for i in s.lower():
        if i == c:
            result += 1
            
    print(c, result)