o = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}

while True:
    s = input()
    
    if s == '#':
        break
    
    result = 0
    
    for i in range(len(s)):
        result += o[s[i]] * (8 ** (len(s) - i - 1))
        
    print(result)