n = int(input())

l = sorted([int(input()) for _ in range(n)], reverse=True)
s = [5 if i >= 250 else 4 if i >= 200 else 3 if i >= 140 else 2 if i >= 100 else 1 if i >= 60 else 0 for i in l]

if n > 42:
    print(sum(l[:42]), sum(s[:42]))
    
else:
    print(sum(l), sum(s))