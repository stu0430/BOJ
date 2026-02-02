n = int(input())

result = 0
for _ in range(n):
    w = input()
    
    stack = []
    
    for i in range(len(w)):
        if not stack:
            stack.append(w[i])
            
        elif w[i] != stack[-1]:
            stack.append(w[i])
            
        else:
            stack.pop()

    if not stack:
        result += 1

print(result)