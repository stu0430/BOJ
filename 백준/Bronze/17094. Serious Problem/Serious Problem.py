n = int(input())
s = input()

a = [0, 0]

for i in s:
    if i == '2':
        a[0] += 1
        
    elif i == 'e':
        a[1] += 1
        
if a[0] > a[1]:
    print('2')
    
elif a[0] < a[1]:
    print('e')
    
else:
    print('yee')