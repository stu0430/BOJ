n, h, w = map(int, input().split())
s = [input() for _ in range(h)]

result = ''

for i in range(n):
    flag = False
    
    for j in range(w * i, w * (i + 1)):
        for k in range(h):
            if s[k][j] != '?':
                result += s[k][j]
                flag = True
                break
            
        if flag:
            break
        
    if not flag:
        result += '?'
        
print(result)
