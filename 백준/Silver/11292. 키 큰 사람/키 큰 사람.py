while True:
    array = []

    n = int(input())
    
    if n == 0:
        break
    
    else:
        for _ in range(n):
            name, height = input().split(' ')
            height = float(height)
            array.append((name, height))

        max_height = max(array, key=lambda x: x[1])[1]

        for i in array:
            if i[1] == max_height:
                print(i[0], end=' ')     
                
        print()