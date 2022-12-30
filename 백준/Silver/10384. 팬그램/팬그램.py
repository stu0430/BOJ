import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = input().rstrip()
        
    array = [0] * 26
    
    for j in s:
        if j.isalpha():
            array[ord(j.lower()) - 97] += 1
            
    if 0 in array:
        print(f'Case {i + 1}: Not a pangram')
        
    elif min(array) == 1:
        print(f'Case {i + 1}: Pangram!')
        
    elif min(array) == 2:
        print(f'Case {i + 1}: Double pangram!!')
        
    elif min(array) == 3:
        print(f'Case {i + 1}: Triple pangram!!!')