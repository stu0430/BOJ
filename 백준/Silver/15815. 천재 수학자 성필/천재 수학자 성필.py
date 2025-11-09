import sys

input = sys.stdin.readline

expression = input().rstrip()
operators = {'+', '-', '*', '/'}
stack = []

for char in expression:
    if char not in operators:
        stack.append(int(char))
    else:
        second = stack.pop()
        first = stack.pop()
        
        if char == '+':
            stack.append(first + second)
            
        elif char == '-':
            stack.append(first - second)
            
        elif char == '*':
            stack.append(first * second)
            
        elif char == '/':
            stack.append(first // second)

print(stack.pop())