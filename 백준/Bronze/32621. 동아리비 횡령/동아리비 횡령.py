s = input().split('+')

result = 'CUTE'

if len(s) != 2:
    result = 'No Money'
    
else:
    x, y = s[0], s[1]
    
    if x != y:
        result = 'No Money'
        
    elif x.startswith('0') and len(x) > 1:
        result = 'No Money'
        
    elif not x.isdigit():
        result = 'No Money'
        
    elif x == '0':
        result = 'No Money'

print(result)