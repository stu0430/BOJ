t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    for i in range(a, 0, -1):
        if a % i == 0 and b % i == 0:
            gcm = i
            break
    lcm = gcm * (a//gcm) * (b//gcm)
    print(lcm)