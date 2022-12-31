import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    
    if s == '#':
        break
        
    array = [0] * 26
    
    for i in s:
        if i.isalpha():
            array[ord(i.lower()) - 97] += 1

            if array[ord(i.lower()) - 97] > 1:
                array[ord(i.lower()) - 97] = 1
            
    print(sum(array))