n = int(input())
for i in range(n):
    word = input()
    word = word.split(' ')
    print(f'Case #{i+1}: ', end='')
    for j in range(len(word)):  
        print(f'{word[-(j+1)]}',end = ' ')
    print()