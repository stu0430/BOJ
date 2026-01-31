import math

xA, yA, xB, yB, xC, yC = map(int, input().split())

if (xB - xA) * (yC - yA) == (yB - yA) * (xC - xA):
    result = -1
else:
    AB = math.hypot(xB - xA, yB - yA)
    BC = math.hypot(xC - xB, yC - yB)
    CA = math.hypot(xA - xC, yA - yC)
    
    perimeter1 = 2 * (AB + CA)
    perimeter2 = 2 * (CA + BC)
    perimeter3 = 2 * (BC + AB)
    
    result = max(perimeter1, perimeter2, perimeter3) - min(perimeter1, perimeter2, perimeter3)

print(result)