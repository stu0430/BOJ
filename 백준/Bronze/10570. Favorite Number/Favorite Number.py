n = int(input())

for _ in range(n):
    v = int(input())
    
    array = [0] * 1001
    
    for _ in range(v):
        s = int(input())
        array[s] += 1
        
    print(array.index(max(array)))