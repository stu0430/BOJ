input()
a,b = 0,0
for i in input():
    if i == 'A':
        a+=1
    else:
        b+=1
if a == b:
    print('Tie')
else:
    print('A' if a > b else 'B')