n = int(input())

s, e = 1, n

while True:
    mid = (s + e) // 2 
    
    if mid ** 2 == n:
        print(mid)
        break
    
    if mid ** 2 > n:
        e = mid
        
    else:
        s = mid