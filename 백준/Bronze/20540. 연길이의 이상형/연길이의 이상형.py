s = set(input())

mbti = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
result = [char for char in mbti if char not in s]
    
print(''.join(result))