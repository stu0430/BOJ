import sys

input = sys.stdin.readline

s = input().rstrip()
h, g = 0, 0 
happy = set('HAPPY')
sad = set('SAD')

for i in s:
    if i in happy:
        h += 1

    if i in sad:
        g += 1

if h == g == 0:
    print('50.00')
else:
    score = h * 10000 / (h + g)
    print(f'{int(score + 0.5) / 100:.2f}')