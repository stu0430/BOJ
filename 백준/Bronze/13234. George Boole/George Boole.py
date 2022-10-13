array = list(input().split())

x1 = array[0]
x2 = array[1]
x3 = array[2]

if x1 == 'false':
    x1 = False
elif x1 == 'true':
    x1 = True

if x3 == 'false':
    x3 = False
elif x3 == 'true':
    x3 = True
    
if x2 == 'AND':
    result = x1 and x3
elif x2 == 'OR':
    result = x1 or x3
    
if result:
    print('true')
else:
    print('false')