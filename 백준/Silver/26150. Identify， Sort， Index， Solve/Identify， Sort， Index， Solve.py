n = int(input())

array = [(s, int(i), int(d)) for s, i, d in (input().split() for _ in range(n))]

array.sort(key=lambda x: (x[1]))

result = ''

for i in array:
    x = i[0][i[2] - 1]
    
    if x.islower():
        x = x.upper()
        
    result += x
    
print(result)