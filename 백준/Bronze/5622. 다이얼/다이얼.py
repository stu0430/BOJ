import sys

input = sys.stdin.readline

word = input().rstrip()

result = 0

for i in range(len(word)):
    
    if ord(word[i]) <= 67:
        result += 3
        
    elif ord(word[i]) <= 70:
        result += 4
        
    elif ord(word[i]) <= 73:
        result += 5
        
    elif ord(word[i]) <= 76:
        result += 6
        
    elif ord(word[i]) <= 79:
        result += 7
        
    elif ord(word[i]) <= 83:
        result += 8
        
    elif ord(word[i]) <= 86:
        result += 9
        
    else:
        result += 10
        
print(result)