import sys

input = sys.stdin.readline

s = list(input().strip())
e = list(input().strip())
stack = []

for char in s:
    stack.append(char)
    
    if stack[-len(e):] == e:
        for _ in range(len(e)):
            stack.pop()
            
if stack:
    print(''.join(stack))
else:
    print('FRULA')