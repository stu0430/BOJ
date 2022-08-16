def Xor(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return (x-1) ^ x
    elif x % 4 == 2:
        return (x-2) ^ (x-1) ^ x
    else:
        return 0

t = int(input())

for i in range(t):
    s, f = map(int, input().split())
    print(Xor(s-1) ^ Xor(f))