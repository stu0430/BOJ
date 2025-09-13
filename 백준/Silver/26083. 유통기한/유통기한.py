import sys

input = sys.stdin.readline

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def able(yy, mm, dd, y, m, d):
    if yy != y:
        return y < yy
    
    if mm != m:
        return m < mm
    
    return d <= dd

y, m, d = map(int, input().split())
n = int(input())

results = []
for _ in range(n):
    a, b, c = map(int, input().split())
    t = [a, b, c, c, b, a, c, a, b]
    
    val = False
    ans = 'invalid'
    
    for i in range(0, 7, 3):
        yy, mm, dd = t[i], t[i + 1], t[i + 2]
        
        if 0 < mm < 13:
            ld = day[mm]
            
            if mm == 2 and yy % 4 == 0:
                ld += 1
                
            if 0 < dd <= ld:
                val = True
                
                if not able(yy, mm, dd, y, m, d):
                    ans = 'unsafe'
                    break
    
    if ans != 'unsafe' and val:
        ans = 'safe'
        
    results.append(ans)

for result in results:
    print(result)