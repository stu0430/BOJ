s = input()
vowels = {'a', 'e', 'i', 'o', 'u'}

array = [i + 1 for i, c in enumerate(s) if c in vowels]

if len(array) == 0:
    print(-1)
    
else:
    if s[-1] in vowels or s[-1] == 'n' or s[-1] == 's':
        if len(array) >= 2:
            print(array[-2])
            
        else:
            print(-1)
            
    else:
        print(array[-1])