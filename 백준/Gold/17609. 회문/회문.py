import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    word = input().rstrip()
    
    l, r = 0, len(word) - 1
    result = 0
    
    for _ in range(len(word)):
        if l >= r:
            break
        
        if word[l] == word[r]:
            l += 1
            r -= 1  
            continue
        
        if word[l] == word[r - 1]:
            temp = word[l:r]
            if temp[:] == temp[::-1]:
                result = 1
                break
        
        if word[l + 1] == word[r]:
            temp = word[l + 1:r + 1]
            if temp[:] == temp[::-1]:
                result = 1
                break
            
        result = 2
        break
        
    print(result)