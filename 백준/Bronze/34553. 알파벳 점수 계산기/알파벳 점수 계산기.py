s = input()

result = 0
score = 1

for i in range(len(s)):
    if i == 0:
        result += 1
        
    else:
        if s[i] > s[i-1]:
            score += 1
            
        else:
            score = 1
            
        result += score

print(result)