import sys

input = sys.stdin.readline

m = int(input())

S = set()

for i in range(m):
    cal = input().rstrip()
    
    if ' ' in cal:
        cal, x = cal.split()
        x = int(x)
    
    if cal == 'add':
        if x in S:
            pass
        else:
            S.add(x)
            
    elif cal == 'remove':
        if x not in S:
            pass
        else:
            S.remove(x)
            
    elif cal == 'check':
        if x in S:
            print(1)
        else:
            print(0)
        
    elif cal == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    
    elif cal == 'all':
        S = set([i for i in range(1,21)])
    
    elif cal == 'empty':
        S = set() 