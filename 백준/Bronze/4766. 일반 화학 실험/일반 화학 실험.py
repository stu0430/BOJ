s = 201

while True:
    t = float(input())
    
    if t == 999:
        break
    
    if s < 201:
        print(f'{t - s:.2f}')
    
    s = t