a, b = map(int, input().split())
x, y = map(int, input().split())
    
if a != 0 and b != 0:
    print(2)
    
elif a < x or b < y:
    print(1)
    
else:
    print(3)