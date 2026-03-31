t = int(input())

for _ in range(t):
    k = int(input())
    array = [input() for _ in range(k)]
    
    found = False
    for i in range(k):
        if found:
            break
        
        for j in range(k):
            if i == j:
                continue
            
            word = array[i] + array[j]
            
            if word == word[::-1]:
                print(word)
                found = True
                break
    
    if not found:
        print(0)