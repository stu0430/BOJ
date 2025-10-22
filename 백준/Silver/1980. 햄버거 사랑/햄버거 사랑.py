n, m, t = map(int, input().split())

if t < min(n, m):
    print(0, t)
    
else:
    flag = False
    
    for i in range(t, 0, -1):
        c = t - i
        
        for j in range(i // max(n, m) + 1):
            tmp = i - (j * max(n, m))
            
            if tmp % min(n, m) == 0:
                b = (tmp // min(n, m)) + j
                print(b, c)
                
                flag = True
                break
            
        if flag:
            break