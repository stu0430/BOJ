N, S, R = map(int, input().split())

s = set(map(int, input().split()))
r = set(map(int, input().split()))  

result = 0

a = s & r
s = list(s - a)
r = list(r - a)

s.sort()

for t in s:
    if t - 1  in r:
        r.remove(t - 1)
        
    elif t + 1 in r:
        r.remove(t + 1)
        
    else:
        result += 1  

print(result)