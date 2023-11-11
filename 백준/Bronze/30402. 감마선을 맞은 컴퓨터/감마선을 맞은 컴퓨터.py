import sys

input = sys.stdin.readline

pixels = [input().rstrip().split() for i in range(15)]

for y in pixels:
    for x in y:
        if x == 'w':
            print('chunbae')
            exit()
        
        elif x == 'b':
            print('nabi')
            exit()

        elif x == 'g':
            print('yeongcheol')
            exit()