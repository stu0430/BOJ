import sys

input = sys.stdin.readline

t, s = map(int, input().split())

if t <= 11:
    t = 'm'
elif 12 <= t <= 16:
    t = 'a'
else:
    t = 'e'
    
if s == 1:
    s = True
else:
    s = False
    
if s or t != 'a':
    print(280)
elif t == 'a' and not s:
    print(320)