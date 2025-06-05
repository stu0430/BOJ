s = input()

d = {'c': 26, 'd': 10}

result = d[s[0]]

for i in range(1, len(s)):
    x = d[s[i]]
    
    if s[i] == s[i - 1]:
        x -= 1
        
    result *= x

print(result)