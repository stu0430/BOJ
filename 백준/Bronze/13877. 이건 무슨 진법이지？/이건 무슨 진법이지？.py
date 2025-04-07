t = int(input())

for _ in range(t):
    k, d = input().split()
    
    o = int(d, 8) if max(list(d)) < '8' else 0
    h = int(d, 16)
    
    print(k, o, int(d), h)