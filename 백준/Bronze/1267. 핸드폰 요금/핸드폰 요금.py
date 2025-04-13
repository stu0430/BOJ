n = int(input())
array = [int(x) for x in input().split()]

y, m  = 0, 0

for i in array:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15
    
if y < m:
    print('Y', y)
    
elif y == m:
    print('Y M', m)
    
else:
    print('M', m)