import sys

input = sys.stdin.readline

n = int(input())
f = int(input())

x = ((n // 100) * 100) % f

if(x == 0):
    print("00")
else:
    if(f - x) // 10 == 0:
        print("0" + str(f - x))
    else:
        print(str(f - x))