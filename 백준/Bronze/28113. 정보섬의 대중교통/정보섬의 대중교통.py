n, a, b = map(int, input().split())

result = 'Bus'

if b < a:
    result = 'Subway'
    
elif a == b:
    result = 'Anything'

print(result)