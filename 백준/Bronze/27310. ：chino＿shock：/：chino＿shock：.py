imoji = input()
result = len(imoji)

for i in imoji:
    if i =='_':
        result += 5
        
    elif i == ':':
        result += 1
        
print(result)