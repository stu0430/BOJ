import sys

input = sys.stdin.readline

l = int(input())

if 620 <= l <= 780:
    print('Red')

elif 590 <= l < 620:
    print('Orange')

elif 570 <= l < 590:
    print('Yellow')

elif 495 <= l < 570:
    print('Green')

elif 450 <= l < 495:
    print('Blue')

elif 425 <= l < 450:
    print('Indigo')

elif 380 <= l < 425:
    print('Violet')