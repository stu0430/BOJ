sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
px, py = map(int, input().split())

if sy == ey:
    sx, sy = sy, sx
    ex, ey = ey, ex
    px, py = py, px

if (sx, sy) > (ex, ey):
    sx, sy, ex, ey = ex, ey, sx, sy

if sx != ex:
    print(1)
    
elif sx != px:
    print(0)
    
elif sy < py and py < ey:
    print(2)
    
else:
    print(0)