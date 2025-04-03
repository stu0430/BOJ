a = int(input())
array = list(map(int, input().split()))
b = int(input())

x = 0
for i in range(a):
    if array[i] != 0 and array[i] <= b:
        x += 1
        
    elif array[i] == 0:
        continue
        
    else:
        if array[i] % b != 0:
            x += (array[i] // b) + 1
            
        else:
            x += (array[i] // b)
            
print(b * x)