import datetime

a, b, c = map(int, input().split())

d, e, f = map(int, input().split())

date1 = datetime.date(a, b, c)
date2 = datetime.date(d, e, f)

if abs(date2 - date1).days < 365243:
    print(f'D-{abs(date2 - date1).days}')
else: 
    print('gg')