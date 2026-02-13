n, p = map(int, input().split())

array = []
temp = n

while True:
    temp = n * temp % p
    
    if temp in array:
        print(len(array) - array.index(temp))
        break
    
    array.append(temp)