import sys

input = sys.stdin.readline

s = input().rstrip()

f = True
for i in range(len(s)):
    if s[0] != s[i]:
        f = False
        break

if f:
    print(-1)
else:
    p = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            p = False
            break
    
    if p:
        print(len(s) - 1)
    else:
        print(len(s))