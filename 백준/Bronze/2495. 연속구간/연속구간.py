for _ in range(3):
    n = input()
    
    result, count = 1, 1 

    for i in range(1, 8):
        if n[i - 1] == n[i]:
            count += 1
            
        else:
            result = max(result, count)
            count = 1
            
    result = max(result, count)
    
    print(result)