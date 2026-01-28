a, d, k = map(int, input().split())

diff = k - a

if (diff % d == 0) and ((diff // d) >= 0):
    print(diff // d + 1)
    
else:
    print('X')