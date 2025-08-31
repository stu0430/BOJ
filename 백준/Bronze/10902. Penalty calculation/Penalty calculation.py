n = int(input())

f = 0
mx = 0
tf = 0
sf = 0

for i in range(1, n + 1):
    t, s = map(int, input().split())
    
    if s > mx:
        mx = s
        f = i
        tf = t
        sf = s

if sf == 0:
    print(0)
    
else:
    print(tf + (f - 1) * 20)