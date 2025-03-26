c = int(input())

result = 0
loop = ['for', 'while']

for _ in range(c):
    count = 0
    code = input()
    
    for l in loop:
        if l in code:
            count += code.count(l)
        
    if count > result:
        result = count
        
print(result)