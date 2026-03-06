t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    while 'ABB' in s:
        s = s.replace('ABB', 'BA', 1)
        
    print(s)