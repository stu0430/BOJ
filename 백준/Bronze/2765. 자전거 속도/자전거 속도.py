i = 1
pi = 3.1415927

while True:
    r, s, t = map(float, input().split())
    
    if s == 0:
        break
    
    distance = r / (5280 * 12) * pi * s
    mph = distance / t * (60 * 60)
    
    print(f'Trip #{i}: {distance:0.2f} {mph:0.2f}')
    
    i += 1