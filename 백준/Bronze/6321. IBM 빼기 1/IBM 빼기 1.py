n = int(input())

for i in range(1, n + 1):
    name = input()
    result = ''
    
    for j in range(len(name)):
        value = ord(name[j]) + 1
        
        if value > 90:
            value = 65
            
        result += chr(value)

    print(f'String #{i}', result, sep='\n')
    print('')