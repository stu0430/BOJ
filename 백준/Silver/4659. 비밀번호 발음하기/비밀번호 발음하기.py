import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    
    if s == 'end':
        break
        
    flag = 0
    count = 0
    
    for i in range(len(s)):
        if s[i] in 'aeiou':
            flag = 1
            count = 0
        else:
            count += 1
            
        if count == 3:
            flag = 2
            break
            
    if flag == 2:
        print(f'<{s}> is not acceptable.')
        continue
    
    if flag == 0:
        print(f'<{s}> is not acceptable.')
        continue
    
    flag = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i] not in 'eo':
            flag = 1
            break
        
    if flag == 1:
        print(f'<{s}> is not acceptable.')
        continue
        
    flag = 0

    for i in range(len(s) - 2):
        if s[i] in 'aeiou' and s[i + 1] in 'aeiou' and s[i + 2] in 'aeiou':
            flag = 1
            break
        
    if flag == 1:
        print(f'<{s}> is not acceptable.')
        continue
    
    print(f'<{s}> is acceptable.')