n = int(input())
result = f'{2 ** -n:.300f}'

last = len(result)
for i in range(last - 1, 1, -1):
    if result[i] != '0':
        last = i
        break
    
print(result[:last+1])